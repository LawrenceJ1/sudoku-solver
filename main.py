#!/usr/bin/env python
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)
        self.canvas.grid()
        
    
app = Application()
app.master.title("Sudoku")
app.mainloop()
