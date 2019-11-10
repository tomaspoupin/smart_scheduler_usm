import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import GUI.ROOT_AND_MAIN.USER_WINDOW.SUBJECT_FRAME.callbacks as callbacks
from GUI.ROOT_AND_MAIN.USER_WINDOW.SUBJECT_FRAME.grid import grid

class Subject_frame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent.frame)

        self.labels = {
            "subscribed subjects": {
                "text": "Ramos Inscritos:"
            },
            "possible subjects": {
                "text": "Ramos:"
            }
        }
        self.buttons = {
            "subscribe": {
                "text": "Inscribir",
                "command": self.subscribe_button_callback
            },
            "unsubscribe": {
                "text": "Desinscribir",
                "command": self.unsubscribe_button_callback
            }
        }
        self.lists = {
            "subscribed subjects": {
                "items": [],
                "listvariable": tk.StringVar(self.frame),
                "height": 7,
                "scrollbar": ttk.Scrollbar(self.frame, orient=tk.VERTICAL)
            },
            "possible subjects": {
                "items": callbacks.get_possible_subjects_list(),
                "listvariable": tk.StringVar(self.frame),
                "height": 7,
                "scrollbar": ttk.Scrollbar(self.frame, orient=tk.VERTICAL)
            }
        }

    def set_widgets(self):
        for label in self.labels:
            self.labels[label]['widget'] = ttk.Label(
                self.frame, # parent
                text=self.labels[label]['text'] # text
            )

        for button in self.buttons:
            self.buttons[button]['widget'] = ttk.Button(
                self.frame,
                text=self.buttons[button]['text'],
                command=self.buttons[button]['command']
            )
        
        for current_list in self.lists:
            self.lists[current_list]['listvariable'].set(
                self.lists[current_list]['items']
                )
            self.lists[current_list]['widget'] = tk.Listbox(
                self.frame,
                height=self.lists[current_list]['height'],
                listvariable=self.lists[current_list]['listvariable']
            )
            # scrollbar config
            self.lists[current_list]['widget']['yscrollcommand'] = \
                self.lists[current_list]['scrollbar'].set
            self.lists[current_list]['scrollbar']['command'] = \
                self.lists[current_list]['widget'].yview
        
        # bind events
        self.frame.bind("<Visibility>", self.update_frame)

    def grid(self):
        self.frame.grid(row=1, column=0, sticky='wens')

        for widget_type in grid:
            for widget_key in grid[widget_type]:
                self.__dict__[widget_type][widget_key]['widget'].grid(
                    row=grid[widget_type][widget_key]["row"],
                    column=grid[widget_type][widget_key]["column"],
                    rowspan=grid[widget_type][widget_key]["rowspan"],
                    columnspan=grid[widget_type][widget_key]["columnspan"],
                    sticky=grid[widget_type][widget_key]["sticky"],
                    padx=grid[widget_type][widget_key]["padx"],
                    pady=grid[widget_type][widget_key]["pady"]
                )
                if widget_type == 'lists':
                    self.lists[widget_key]['scrollbar'].grid(
                        row=grid[widget_type][widget_key]["row"],
                        column=grid[widget_type][widget_key]["column"] + 1,
                        rowspan=grid[widget_type][widget_key]["rowspan"],
                        columnspan=grid[widget_type][widget_key]["columnspan"],
                        sticky='wns'
                    )

    # CALLBACKS

    def subscribe_button_callback(self):
        selection = \
            self.lists['possible subjects']['widget'].get(tk.ANCHOR)
        if not selection:
            messagebox.showinfo(
                title='Inscribir Asignatura',
                message='No hay asignaturas para inscribir'
            ) 
        elif selection in self.lists['subscribed subjects']['items']:
            messagebox.showinfo(
                title='Inscribir Asignatura',
                message='Esta asignatura ya fue inscrita'
            )          
        else:
            self.lists['subscribed subjects']['items'].append(selection)
            self.lists['subscribed subjects']['listvariable'].set(
                self.lists['subscribed subjects']['items']
            )
            callbacks.subscribe_subject(
                self.get_current_user(),
                selection
            )
    
    def unsubscribe_button_callback(self):
        selection = \
            self.lists['subscribed subjects']['widget'].get(tk.ANCHOR)
        if not selection:
            messagebox.showinfo(
                title='Inscribir Asignatura',
                message='No hay asignaturas para desinscribir'
            )
        else:
            self.lists['subscribed subjects']['items'].remove(selection)
            self.lists['subscribed subjects']['listvariable'].set(
                self.lists['subscribed subjects']['items']
            )
            callbacks.unsubscribe_subject(
                self.get_current_user(),
                selection
                )

    def get_current_user(self):
        return self.parent.children['user_child'].current_user
    
    def refresh_possible_subjects_list(self):
        self.lists["possible subjects"]["items"] = \
            callbacks.get_possible_subjects_list()
        self.lists['possible subjects']['listvariable'].set(
            self.lists["possible subjects"]["items"]
        )

    def update_frame(self, ve):
        self.refresh_possible_subjects_list()