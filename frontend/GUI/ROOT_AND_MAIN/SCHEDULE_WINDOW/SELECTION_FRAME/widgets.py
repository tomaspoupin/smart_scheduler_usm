import tkinter as tk
from tkinter import ttk

import ROOT_AND_MAIN.SCHEDULE_WINDOW.SELECTION_FRAME.callbacks as callbacks
from ROOT_AND_MAIN.SCHEDULE_WINDOW.SELECTION_FRAME.grid import grid


class Selection_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

        self.labels = {
            'overlaps': {
                'text': 'Topes:'
            },
            'options': {
                'text': 'Opción:'
            }
        }

        self.comboboxes = {
            'overlaps': {
                'items': ['0','1','2','3'],
                'textvariable': tk.StringVar(self.frame)
            },
            'options': {
                'items': ['1','2','3','4','5'],
                'textvariable': tk.StringVar(self.frame)
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

#    # CALLBACKS
#    def new_schedule_option(self):
#        pass