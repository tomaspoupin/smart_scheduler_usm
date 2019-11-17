import tkinter as tk
from tkinter import ttk

class Root_and_main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Smart Scheduler USM")
        self.main_frame = ttk.Frame(self.root)
        self.window_manager = ttk.Notebook(self.main_frame)

        self.parent = None
        self.children = {}

    def grid(self):
        self.root.grid()
        self.main_frame.grid(sticky='wens')
        self.window_manager.grid(sticky='wens')

    def add_children(self, **kwargs):
        for child in kwargs:
            self.children[child] = kwargs[child]

    def set_events(self):
        self.window_manager.bind('<<NotebookTabChanged>>', self.tab_change_callback)

    def tab_change_callback(self, ve):
        tab_index = self.window_manager.index(self.window_manager.select())
        if tab_index == 2:
            self.children['schedule_window_child'].children['user_child'].update_user_frame()    
        if self.children['schedule_window_child'].children['info_child'].hide_info == False:
            self.children['schedule_window_child'].children['info_child'].change_info_frame_visibility()

    def run(self):
        self.root.mainloop()