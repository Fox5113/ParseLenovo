from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import json


class Laptop:
    def __init__(self, name, href, model):
        self.name = name
        self.href = href
        self.model = model


class Models:
    def __init__(self, models):
        self.allmodel = models

    def __str__(self):
        return "name : " + self.name + " href : " + self.href


def filter_empty_item(web_element):
    return len(web_element.text) > 0


if __name__ == '__main__':
    driver = webdriver.Firefox()
    # firefox_options = Options()
    # firefox_options.set_headless()
    # driver = webdriver.Firefox(options=firefox_options)
    driver.get("https://www.lenovo.com/by/ru/laptops/c/Laptops#view-all")
    driver.maximize_window()
    tags = ['THINKPAD', 'ThinkBook Laptops: ', 'IDEAPAD: ', 'LENOVO: ', 'YOGA: ',
            'Игровые ноутбуки Lenovo Legion: Lenovo Legion Logo']
    all_laptop = list()
    laptops = list()
    for tag in tags:
        category = driver.find_element(By.XPATH, f"//img[@alt='{tag}']")
        category.click()
        models_in_category = list(filter(filter_empty_item, (driver.find_elements(By.XPATH,
                                                                                  "//div[@class='model-title']/a"))))
        for model in models_in_category:
            print(model.text)
        all_laptop.extend(Models(list(filter(filter_empty_item,
                                             driver.find_elements(By.XPATH, "//a[@class='vam-subseries']")))))

        for model in all_laptop:
            item = Laptop(model.text, model.get_dom_attribute("href"))
            laptops.append(item)

        for item in laptops:
            print(item)

    result = json.dumps(laptops)
    driver.close()
