# fruits = ["apple", "orange", "banana", "grape", "strawberry"]
# fruits.append('mango')
# fruits.pop
# # fruits
# print(fruits)

from contextlib import closing
from selenium import webdriver
from selenium.webdriver import Chrome # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
url='https://openmobile.ipass.com/euservices/activation/?companyId=1043128#/creditCardForm?lang=en'

# use firefox to get page with javascript generated content
# /Users/fguo/Downloads  driver = webdriver.Chrome('/path/to/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
with closing(webdriver.Chrome('/Users/fguo/Downloads/chromedriver', chrome_options=options)) as browser:
    browser.get(url)

    # wait for the page to load
    WebDriverWait(browser, timeout=10).until(
        lambda x: x.find_element_by_id('purchaseForm'))
    # store it to string variable
    page_source = browser.page_source
print(page_source)
