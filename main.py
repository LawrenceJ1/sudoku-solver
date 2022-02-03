#!/usr/bin/env python
import tkinter as tk

class Application(tk.Frame):    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.width = 800
        self.height = 600
        self.createWidgets()
        
    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)
        self._drawGrid()
        
    def _drawGrid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "grey"
            self.canvas.create_line(i*(self.width/9), 0, i*(self.width/9), self.height, fill=color)
            self.canvas.create_line(0, i*(self.height/9), self.width, i*(self.height/9), fill=color)
        
app = Application()
app.master.title("Sudoku")
app.mainloop()
