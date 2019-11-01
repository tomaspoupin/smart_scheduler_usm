import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import GUI.ROOT_AND_MAIN.USER_WINDOW.USER_FRAME.callbacks as callbacks
from GUI.ROOT_AND_MAIN.USER_WINDOW.USER_FRAME.grid import grid


class User_frame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent.frame)

        # state variables
        self.current_user = None

        self.labels = {
            'new user': {
                'text': 'Agregar usuario:'
            },
            'select user': {
                'text': 'Seleccionar usuario:'
            }
        }
        self.entries = {
            'new user': {
                'textvariable': tk.StringVar(self.frame)
            }
        }
        self.buttons = {
            'submit user': {
                'text': 'Ingresar',
                'command': self.new_user_callback
            },
            "delete user": {
                "text": "Eliminar",
                "command": self.delete_user_button_callback
            }
        }
        self.comboboxes = {
            'users combobox': {
                'items': callbacks.get_user_list(),
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
                if combobox == 'users combobox':
                    self.current_user = \
                        self.comboboxes[combobox]['textvariable'].get()
        self.set_subscribed_subject_list_to_current_user()

        # Set users combobox selection event
        self.comboboxes['users combobox']['widget'].bind(
            "<<ComboboxSelected>>", self.user_selected_callback
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
    def new_user_callback(self):
        new_user = self.entries['new user']['textvariable'].get().strip().capitalize()
        if new_user in self.comboboxes['users combobox']['items']:
            messagebox.showinfo(
                title='Nuevo Usuario',
                message='Este usuario ya existe'
            )
            self.entries['new user']['textvariable'].set('')
            return

        new_user = callbacks.validate_user(new_user)

        if isinstance(new_user, str):
            anwser = messagebox.askyesno(
                message='Estas segure que quieres agregar a {}?'.format(new_user),
                title='Agregar nuevo usuario'
            )
            if anwser:
                self.comboboxes['users combobox']['items'].append(new_user)
                self.comboboxes['users combobox']['widget']['values'] = \
                    self.comboboxes['users combobox']['items']
                self.comboboxes['users combobox']['textvariable'].set(new_user)
                self.entries['new user']['textvariable'].set('')
                self.current_user = \
                    self.comboboxes['users combobox']['textvariable'].get()
                callbacks.add_new_user(new_user)
                self.set_subscribed_subject_list_to_current_user()
                
            else:
                return

        else:
            messagebox.showinfo(
                title='Nuevo Usuario',
                message=new_user[0]
            )
            self.entries['new user']['textvariable'].set('')

    def delete_user_button_callback(self):
        user_to_delete = self.comboboxes['users combobox']['textvariable'].get()
        if not user_to_delete:
            messagebox.showinfo(
                title='Eliminar usuario',
                message='No hay usuarios para eliminar'
            )
        else:
            anwser = messagebox.askyesno(
                message='Estas segure que quieres eliminar a {}?'.format(user_to_delete),
                title='Eliminar usuario'
            )
            if anwser:
                self.comboboxes['users combobox']['items'].remove(user_to_delete)
                self.comboboxes['users combobox']['widget']['values'] = \
                    self.comboboxes['users combobox']['items']

                if not self.comboboxes['users combobox']['items']:
                    self.comboboxes['users combobox']['textvariable'].set('')
                    self.current_user = None
                else:
                    self.comboboxes['users combobox']['textvariable'].set(
                        self.comboboxes['users combobox']['items'][0]
                    )
                    self.current_user = \
                        self.comboboxes['users combobox']['textvariable'].get()
                callbacks.remove_user(user_to_delete)
                self.set_subscribed_subject_list_to_current_user()

            else:
                pass
    
    def user_selected_callback(self, ve):
        self.current_user = \
            self.comboboxes['users combobox']['textvariable'].get()
        self.set_subscribed_subject_list_to_current_user()
    
    def set_subscribed_subject_list_to_current_user(self):
        user_subject_list = []
        if self.current_user is not None:
            user_subject_list = callbacks.get_user_subjects_list(self.current_user)

        self.parent.children['subject_child'].lists['subscribed subjects']['items'] = \
            user_subject_list
        self.parent.children['subject_child'].lists['subscribed subjects']['listvariable'].set(
            user_subject_list
            )