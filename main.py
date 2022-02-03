#!/usr/bin/env python
import tkinter as tk
from solver import Solution

class Sudoku(tk.Frame):    
    def __init__(self, master=None):
        #declaring variables
        self.row = self.col = -1
        self.margin = 20
        self.side = 60 
        self.width = self.height = self.margin * 2 + self.side * 9
        self.nums = set()
        for i in range(1, 10):
            self.nums.add(str(i))
        self.board = [[".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(9)]
        self.solver = Solution()
        
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)
        self.solve_button = tk.Button(self, text="Solve", command=self._solve)
        self.solve_button.pack(fill=tk.BOTH, side=tk.BOTTOM)
        
        self._drawGrid()
        self._drawSudoku()
        
        self.canvas.bind("<Button-1>", self._click)
        self.canvas.bind("<Key>", self._key)
        
    def _drawGrid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "grey"
            self.canvas.create_line(self.margin+i*(self.side), self.margin, self.margin+i*(self.side), self.height-self.margin, fill=color)
            self.canvas.create_line(self.margin, self.margin+i*(self.side), self.width-self.margin, self.margin+i*(self.side), fill=color)
    
    def _drawSudoku(self):
        self.canvas.delete("nums")
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != ".":
                    x = self.margin+j*self.side+self.side/2
                    y = self.margin+i*self.side+self.side/2
                    self.canvas.create_text(x, y, text=self.board[i][j], tags="nums", fill="black")
                    
    def _click(self, event):
        if (self.margin < event.x < self.width - self.margin and self.margin < event.y < self.height - self.margin):
            self.canvas.focus_set()
            row, col = int((event.y - self.margin) / self.side), int((event.x - self.margin) / self.side)
            if (self.row, self.col) == (row, col):
                self.row = self.col = -1
            else:
                self.row = row
                self.col = col
        else:
            self.row = self.col = -1
    
    def _key(self, event):
        if self.row != -1 and self.col != -1 and event.char in self.nums:
            self.board[self.row][self.col] = event.char
            self._drawSudoku()
    
    def _solve(self):
        self.solver.solve_sudoku(self.board)
        self._drawSudoku()
        
app = Sudoku()
app.master.title("Sudoku")
app.mainloop()
