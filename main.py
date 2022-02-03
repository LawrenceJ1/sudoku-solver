#!/usr/bin/env python
import tkinter as tk

class Sudoku(tk.Frame):    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.margin = 20
        self.side = 60 
        self.width = self.height = self.margin * 2 + self.side * 9 
        self.createWidgets()
        
    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)
        self._drawGrid()
        
    def _drawGrid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "grey"
            self.canvas.create_line(self.margin+i*(self.side), self.margin, self.margin+i*(self.side), self.height-self.margin, fill=color)
            self.canvas.create_line(self.margin, self.margin+i*(self.side), self.width-self.margin, self.margin+i*(self.side), fill=color)
        
app = Sudoku()
app.master.title("Sudoku")
app.mainloop()
