from selenium import webdriver
from bs4 import BeautifulSoup as soup
from time import sleep

#initializing the webdriver
driver = webdriver.Chrome()
driver.get("https://www.websudoku.com/")
driver.switch_to.frame(0)

#getting puzzle info
page = soup(driver.page_source, features="html.parser")
print(page.find("table", {"id":"puzzle_grid"}))
driver.close()
