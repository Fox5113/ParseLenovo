import json
import pickle
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Laptop:
    def __init__(self, name, href):
        self.name = name
        self.href = href
        self.features = dict()

    def __str__(self):
        return "name : " + self.name + " href : " + self.href


class Models:
    def __init__(self, models):
        self.models = models


def filter_empty_item(web_element):
    return len(web_element.text) > 0


def get_laptop_features(driver, laptop):
    driver.get(r"https://www.lenovo.com" + laptop.href)
    item = list(filter(filter_empty_item, driver.find_elements(By.XPATH, "//tbody/tr/td")))
    return item


def obj_dict(obj):
    return obj.__dict__


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.lenovo.com/by/ru/laptops/c/Laptops#view-all")
    driver.maximize_window()
    tags = ["THINKPAD: ", "ThinkBook Laptops: ", "IDEAPAD: ", "LENOVO: ", "YOGA: ",
            "Игровые ноутбуки Lenovo Legion: Lenovo Legion Logo"]
    all_laptop = list()
    laptops = list()
    for tag in tags:
        category = driver.find_element(By.XPATH, f"//img[@alt='{tag}']")
        category.click()
        models_in_category = list(filter(filter_empty_item, (driver.find_elements(By.XPATH,
                                                                                  "//div[@class='model-title']/a"))))
        laptop_from_page = Models(list(filter(filter_empty_item,
                                              driver.find_elements(By.XPATH, "//a[@class='vam-subseries']"))))
        all_laptop.extend(laptop_from_page.models)

        for model in all_laptop:
            if len(model.text) > 0:
                item = Laptop(model.text, model.get_dom_attribute("href"))
                laptops.append(item)
    for laptop in laptops:
        features = list()
        while True:
            try:
                features = get_laptop_features(driver, laptop)
                break
            except Exception:
                sleep(5)
        driver.delete_all_cookies()
        for i in range(0, len(features) - 2, 2):
            laptop.features[features[i].text] = features[i + 1].text
    driver.close()
    with open('data.json', 'w') as f:
        json_string = json.dumps(laptops, default=obj_dict)
        f.write(json_string)
