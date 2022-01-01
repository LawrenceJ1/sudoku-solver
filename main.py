from selenium import webdriver
from bs4 import BeautifulSoup as soup
from my_leetcode_solution import Solution

#initialization
driver = webdriver.Chrome()
driver.get("https://www.websudoku.com/")
driver.switch_to.frame(0)

#getting puzzle info
page = soup(driver.page_source, features="html.parser")
sudoku = page.find("table", {"id":"puzzle_grid"})
rows = sudoku.find_all("tr")

#saving each value in a matrix
matrix = []
for row in range(len(rows)):
    matrix.append([])
    for col in rows[row].find_all("td"):
        try:
            matrix[row].append(col.input["value"])
        except:
            matrix[row].append(".")

#solve sudoku
solution = Solution()
solution.solve_sudoku(matrix)

#input answer
table = driver.find_elements_by_xpath('//table[@id="puzzle_grid"]//tbody//tr//td//input')
for row in range(9):
    for col in range(9):
        try:
            table[row*9+col].send_keys(matrix[row][col])
        except:
            pass
# driver.close()
