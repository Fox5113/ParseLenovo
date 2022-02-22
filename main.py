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
    thinkpad = driver.find_element(By.XPATH, "//img[@alt='THINKPAD: ']")
    thinkpad.click()
    allmodels_name = list(filter(filter_empty_item, (driver.find_elements(By.XPATH, "//div[@class='model-title']/a"))))

    for model in allmodels_name:

        print(model.text)
    all_laptop = Models(list(filter(filter_empty_item,
                                    driver.find_elements(By.XPATH, "//a[@class='vam-subseries']"))))
    laptops = list()
    for model in all_laptop:
        item = Laptop(model.text, model.get_dom_attribute("href"))
        laptops.append(item)

    for item in laptops:
        print(item)

    result = json.dumps(laptops)
    driver.close()
