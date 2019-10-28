import tkinter as tk
from tkinter import ttk

import ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.callbacks as callbacks
from ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.grid import grid


class User_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        self.labels = {
            'user': {
                'text': 'Usuario:'
            }
        }

        self.comboboxes = {
            'user': {
                'items': ['Sopin', 'Luciano', 'Francisco', 'Mio'],
                'textvariable': tk.StringVar(self.frame)
            }
        } 
        self.buttons = {
            'calculate': {
                'text': 'Calcular Horarios',
                'command': self.calculate_schedule_options
            }
        } 


    def set_widgets(self):
        # set labels
        for label in self.labels:
            self.labels[label]['widget'] = ttk.Label(
                self.frame, # parent
                text=self.labels[label]['text'] # text
            )

        # set comboboxes
        for combobox in self.comboboxes:
            self.comboboxes[combobox]['widget'] = ttk.Combobox(
                self.frame,
                textvariable=self.comboboxes[combobox]['textvariable'],
                values=self.comboboxes[combobox]['items']
            )

        # set buttons
        for button in self.buttons:
            self.buttons[button]['widget'] = ttk.Button(
                self.frame,
                text=self.buttons[button]['text'],
                command=self.buttons[button]['command']
            )

    def grid(self):
        self.frame.grid(row=0, column=0)

        for widget_type in grid:
            for widget_key in grid[widget_type]:
                self.__dict__[widget_type][widget_key]['widget'].grid(
                    row=grid[widget_type][widget_key]["row"],
                    column=grid[widget_type][widget_key]["column"],
                    sticky=grid[widget_type][widget_key]["sticky"],
                    padx=grid[widget_type][widget_key]["padx"],
                    pady=grid[widget_type][widget_key]["pady"]
                )

    # CALLBACKS
    def calculate_schedule_options(self):
        pass