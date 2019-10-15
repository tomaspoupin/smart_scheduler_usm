import tkinter as tk
from tkinter import ttk

class User_window: 
    def __init__(self, parent):
        self.window = ttk.Frame(parent)
    
    def grid(self):
        self.window.grid()