import tkinter as tk
from tkinter import ttk

import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.JSON_callbacks as json_callbacks
import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.widget_callbacks as widget_callbacks
from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.grid import grid
from smart_scheduler_tools import user as user_tools


class User_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent.frame)
        self.parent = parent
        self.current_user = None
        self.users = []

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

        # set buttons
        for button in self.buttons:
            self.buttons[button]['widget'] = ttk.Button(
                self.frame,
                text=self.buttons[button]['text'],
                command=self.buttons[button]['command']
            )
        
        # events binding
        self.comboboxes['user']['widget'].bind(
            "<<ComboboxSelected>>",
            self.user_selected_callback
            )
        self.frame.bind("<Visibility>", self.update_frame)

        self.set_schedule_options_to_current_user()

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

    def calculate_schedule_options(self):
        if self.current_user is None:
            return
        for user in self.users:
            if self.current_user == user.get_name():
                widget_callbacks.calculate_schedule_options(user)
                self.set_schedule_options_to_current_user()
                self.parent.children['selection_child'].update_schedule()
                self.parent.children['info_child'].update_user_info(self.current_user)
                self.parent.children['info_child'].update_gui_info_to_current_user_option()
                return
        new_user = user_tools.User(self.current_user)
        self.users.append(new_user)
        widget_callbacks.calculate_schedule_options(new_user)
        self.set_schedule_options_to_current_user()
        self.parent.children['selection_child'].update_schedule()
        self.parent.children['info_child'].update_user_info(self.current_user)
        self.parent.children['info_child'].update_gui_info_to_current_user_option()

    def user_selected_callback(self, ve):
        self.current_user = \
            self.comboboxes['user']['textvariable'].get()
        self.set_schedule_options_to_current_user()
        self.parent.children['selection_child'].update_schedule()   
        self.parent.children['info_child'].update_gui_info_to_current_user_option()
    
    def set_schedule_options_to_current_user(self):
        self.parent.children['selection_child'].comboboxes['overlaps']['items'] = []
        self.parent.children['selection_child'].comboboxes['overlaps']['widget']['values'] = \
            self.parent.children['selection_child'].comboboxes['overlaps']['items']
        self.parent.children['selection_child'].comboboxes['overlaps']['textvariable'].set('')

        self.parent.children['selection_child'].comboboxes['options']['items'] = []
        self.parent.children['selection_child'].comboboxes['options']['widget']['values'] = \
            self.parent.children['selection_child'].comboboxes['options']['items']
        self.parent.children['selection_child'].comboboxes['options']['textvariable'].set('')
        
        self.buttons['calculate']['text'] = 'Calcular Horarios'
        self.buttons['calculate']['widget']['text'] = self.buttons['calculate']['text']

        self.parent.children['selection_child'].update_schedule()
        if self.current_user is None:
            return
        for user in self.users:
            if self.current_user == user.get_name():
                if user.has_schedule_options():
                    self.parent.children['selection_child'].comboboxes['overlaps']['items'] = \
                        user.get_overlaps_list()
                    self.parent.children['selection_child'].comboboxes['overlaps']['widget']['values'] = \
                        self.parent.children['selection_child'].comboboxes['overlaps']['items']
                    self.parent.children['selection_child'].comboboxes['overlaps']['textvariable'].set(
                        self.parent.children['selection_child'].comboboxes['overlaps']['items'][0]
                    )
                    self.buttons['calculate']['text'] = 'Recalcular Horarios'
                    self.buttons['calculate']['widget']['text'] = self.buttons['calculate']['text']

                    self.parent.children['selection_child'].comboboxes['options']['items'] = \
                        user.get_options_list(
                            self.parent.children['selection_child'].comboboxes['overlaps']['items'][0]
                            )
                    self.parent.children['selection_child'].comboboxes['options']['widget']['values'] = \
                        self.parent.children['selection_child'].comboboxes['options']['items']
                    self.parent.children['selection_child'].comboboxes['options']['textvariable'].set(
                        self.parent.children['selection_child'].comboboxes['options']['items'][0]    
                    )
                return
    
    def update_frame(self, ve):
        self.comboboxes['user']['items'] = json_callbacks.get_user_list()
        self.comboboxes['user']['widget']['values'] = \
            self.comboboxes['user']['items']