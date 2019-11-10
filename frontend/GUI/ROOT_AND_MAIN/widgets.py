import tkinter as tk
from tkinter import ttk

class Root_and_main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Smart Scheduler USM")
        self.main_frame = ttk.Frame(self.root)
        self.window_manager = ttk.Notebook(self.main_frame)

    def grid(self):
        self.root.grid()
        self.main_frame.grid(sticky='wens')
        self.window_manager.grid(sticky='wens')
    
    def run(self):
        self.root.mainloop()