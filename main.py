#!/usr/bin/env python
import tkinter as tk

class Sudoku(tk.Frame):    
    def __init__(self, master=None):
        self.row = self.col = -1
        self.margin = 20
        self.side = 60 
        self.width = self.height = self.margin * 2 + self.side * 9
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)
        
        self._drawGrid()
        self.canvas.bind("<Button-1>", self._click)
        self.canvas.bind("<Key>", self._key)
        
    def _drawGrid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "grey"
            self.canvas.create_line(self.margin+i*(self.side), self.margin, self.margin+i*(self.side), self.height-self.margin, fill=color)
            self.canvas.create_line(self.margin, self.margin+i*(self.side), self.width-self.margin, self.margin+i*(self.side), fill=color)
    
    def _click(self, event):
        if (self.margin < self.x < self.width - self.margin and self.margin < self.y < self.height - self.margin):
            row, col = (event.y - self.margin) / self.side, (event.x - self.margin) / self.side
            if (self.row, self.col) == (row, col):
                self.row = self.col = -1
            else:
                self.row = row
                self.col = col
        else:
            self.row = self.col = -1
    
app = Sudoku()
app.master.title("Sudoku")
app.mainloop()
