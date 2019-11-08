import tkinter as tk
from tkinter import ttk

import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.SELECTION_FRAME.widget_callbacks as widget_callbacks
from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.SELECTION_FRAME.grid import grid


class Selection_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent.frame)
        self.parent = parent

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
                'items': [],
                'textvariable': tk.StringVar(self.frame)
            },
            'options': {
                'items': [],
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
                values=self.comboboxes[combobox]['items'],
                width = 28,
                state='readonly'
            )
        # bind events
        self.comboboxes['overlaps']['widget'].bind(
            "<<ComboboxSelected>>",
            self.overlap_selected_callback
            )
        self.comboboxes['options']['widget'].bind(
            "<<ComboboxSelected>>",
            self.options_selected_callback
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

    def overlap_selected_callback(self, ve):
        active_user = None
        overlaps = self.comboboxes['overlaps']['textvariable'].get()
        self.comboboxes['options']['items'] = []
        self.comboboxes['options']['widget']['values'] = \
            self.comboboxes['options']['items']
        self.comboboxes['options']['textvariable'].set('')
        if not overlaps:
            return
        for user in self.parent.children['user_child'].users:
            if self.parent.children['user_child'].current_user == user.get_name():
                active_user = user
                break
        if active_user is not None:
            self.comboboxes['options']['items'] = \
                user.get_options_list(int(overlaps))
            self.comboboxes['options']['widget']['values'] = \
                self.comboboxes['options']['items']
            self.comboboxes['options']['textvariable'].set(
                self.comboboxes['options']['items'][0]
            )
        self.update_schedule()

    def options_selected_callback(self, ve):
        self.update_schedule()

    def update_schedule(self):
        active_user = None
        for user in self.parent.children['user_child'].users:
            if self.parent.children['user_child'].current_user == user.get_name():
                active_user = user
                break
        if active_user is not None:
            self.parent.children['schedule_child'].current_schedule_dict = \
                active_user.get_schedule_as_dict(
                    self.comboboxes['overlaps']['textvariable'].get(),
                    self.comboboxes['options']['textvariable'].get()
                )
            # for day in self.parent.children['schedule_child'].current_schedule_dict:
            #     for block_index in range(len(day)):
            #         if day[block_index] == 0:
            #             self.parent.children['schedule_child'].current_schedule_labels[day][block_index] = ''
            #         elif day[block_index] == 1:   
            #             pass
            #         else:
            #             self.parent.children['schedule_child'].current_schedule_labels[day][block_index] = \
            #                 '{} ramos'.format(day[block_index])
            self.parent.children['schedule_child'].update_schedule_colors()