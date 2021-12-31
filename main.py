from selenium import webdriver
from bs4 import BeautifulSoup as soup

driver = webdriver.Chrome()
driver.get("https://www.websudoku.com/")
