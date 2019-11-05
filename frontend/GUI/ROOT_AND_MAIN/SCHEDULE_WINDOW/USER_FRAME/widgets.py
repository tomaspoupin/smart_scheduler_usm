import tkinter as tk
from tkinter import ttk

import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.JSON_callbacks as json_callbacks
import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.widget_callbacks as widget_callbacks
from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.grid import grid


class User_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent.frame)
        self.current_user = None

        self.labels = {
            'user': {
                'text': 'Usuario:'
            }
        }

        self.comboboxes = {
            'user': {
                'items': json_callbacks.get_user_list(),
                'textvariable': tk.StringVar(self.frame)
            }
        } 
        self.buttons = {
            'calculate': {
                'text': 'Calcular Horarios',
                'command': widget_callbacks.calculate_schedule_options
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
                values=self.comboboxes[combobox]['items'],
                state='readonly'
            )
            # Set default value for combobox
            if not self.comboboxes[combobox]['items']:
                self.comboboxes[combobox]['textvariable'].set('')
            else:
                self.comboboxes[combobox]['textvariable'].set(
                    self.comboboxes[combobox]['items'][0]
                )
                if combobox == 'user':
                    self.current_user = \
                        self.comboboxes[combobox]['textvariable'].get()
            # Set users combobox selection event
            self.comboboxes['user']['widget'].bind(
            "<<ComboboxSelected>>", widget_callbacks.user_selected_callback
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

