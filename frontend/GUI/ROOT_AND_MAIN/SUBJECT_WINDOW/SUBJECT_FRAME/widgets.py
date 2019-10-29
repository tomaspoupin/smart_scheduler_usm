import tkinter as tk
from tkinter import ttk

import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.callbacks as callbacks
from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.grid import grid


class Subject_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        self.labels = {
            'subject code': {
                'text': 'Código:'
            },
            'section': {
                'text': 'Paralelo:'
            }
        }
        self.entries = {
            'subject code': {
                'textvariable': tk.StringVar(self.frame)
            },
            'section': {
                'textvariable': tk.StringVar(self.frame)
            }
        }
        self.buttons = {
            'submit schedule': {
                'text': 'Ingresar',
                'command': self.new_schedule_option
            }
        }    

    def set_widgets(self):
        # set labels
        for label in self.labels:
            self.labels[label]['widget'] = ttk.Label(
                self.frame, # parent
                text=self.labels[label]['text'] # text
            )
        # set entries
        for entry in self.entries:
            self.entries[entry]['widget'] = ttk.Entry(
                self.frame,
                textvariable=self.entries[entry]['textvariable']
            )
        # set buttons
        for button in self.buttons:
            self.buttons[button]['widget'] = ttk.Button(
                self.frame,
                text=self.buttons[button]['text'],
                command=self.buttons[button]['command']
            )


    def grid(self):
        self.frame.grid(row=1, column=0)

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
    def new_schedule_option(self):
        pass