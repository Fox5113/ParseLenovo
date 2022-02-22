from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


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
    allmodels_name = (driver.find_elements(By.XPATH, "//div[@class='model-title']/a"))
    allmodels_name = list(filter(filter_empty_item, allmodels_name))
    for model in allmodels_name:
        print(model.text)
    driver.close()
