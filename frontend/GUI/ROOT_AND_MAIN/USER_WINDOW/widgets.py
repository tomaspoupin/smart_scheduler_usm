import tkinter as tk
from tkinter import ttk

class User_window: 
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.children = {}
    
    def grid(self):
        self.frame.grid(sticky='wens')

    def add_children(self, **kwargs):
        for child in kwargs:
            self.children[child] = kwargs[child]