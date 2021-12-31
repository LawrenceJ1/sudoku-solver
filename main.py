from selenium import webdriver
from bs4 import BeautifulSoup as soup
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.websudoku.com/")
driver.switch_to.frame(0)
page = soup(driver.page_source, features="html.parser")
print(page)
driver.close()
