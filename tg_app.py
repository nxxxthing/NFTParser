# Load selenium components
import os
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pandas as pd

data = pd.read_csv('content.csv', sep=';')
url_list = data['url'].values
price_list = data['price'].values


result = {}
already_posted = []


def parse_link(url_link, price_class):
    global result

    # Establish chrome driver and go to report site URL
    url = url_link
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-sh-usage")

    # driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver.get(url)

    driver.find_element_by_css_selector(
        '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary').click()

    dropList = Select(driver.find_element_by_css_selector(
        '.MuiNativeSelect-root-178.MuiNativeSelect-select-179.MuiInputBase-input-207.MuiInput-input-195.MuiInputBase-inputMarginDense-208.MuiInput-inputMarginDense-196'))

    dropList.select_by_value('3')


    # price = driver.find_elements_by_class_name(str(price_class))
    price = WebDriverWait(driver, 5).until(lambda x: x.find_elements_by_class_name(price_class))
    name = WebDriverWait(driver, 5).until(lambda x: x.find_elements_by_class_name('card-title.h5'))
    if len(price) < 2:
        print("ERROR!!! on " + url_link, price_class)
        return
    if float(price[0].get_attribute("innerText").split()[0]) * 1.3 <= float(price[1].get_attribute("innerText").split()[0]):
        message = price[0].get_attribute("innerText") + " " + name[0].get_attribute("innerText") + " vs " + price[1].get_attribute("innerText") + " " + name[1].get_attribute("innerText") + " " + url_link
        message = str.replace(message, '#', ' ')
        # print(message)
        if message not in already_posted:
            if url_link not in result:
                result[url_link] = [message]
            else:
                result[url_link].append(message)
            already_posted.append(message)
    sys.exit()
