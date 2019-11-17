import tkinter as tk
from tkinter import ttk

class Subject_window():
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.parent = parent
        self.children = {}

    def grid(self):
        self.frame.grid()

    def add_children(self, **kwargs):
        for child in kwargs:
            self.children[child] = kwargs[child]