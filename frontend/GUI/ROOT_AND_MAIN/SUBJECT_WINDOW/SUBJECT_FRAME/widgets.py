import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.callbacks as callbacks
from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.grid import grid

class Subject_frame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent.frame)

        self.current_subject = None
        self.current_section = None

        self.labels = {
            'subject code': {
                'text': 'Código:'
            },
            'section': {
                'text': 'Paralelo:'
            }
        }
        self.comboboxes = {
            'subject code': {
                'items': callbacks.get_subject_list(),
                'textvariable': tk.StringVar(self.frame)
            },
            'section': {
                'items': callbacks.get_section_list(self.current_subject), 
                'textvariable': tk.StringVar(self.frame)
            }
        }
        self.buttons = {
            'submit schedule': {
                'text': 'Ingresar',
                'command': self.new_schedule_option
            },
            'delete schedule': {
                'text': 'Borrar',
                'command': self.delete_schedule_option
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
                state='normal'
            )
        # set buttons
        for button in self.buttons:
            self.buttons[button]['widget'] = ttk.Button(
                self.frame,
                text=self.buttons[button]['text'],
                command=self.buttons[button]['command']
            )

        # Set subjects combobox selection event
        self.comboboxes['subject code']['widget'].bind(
            "<<ComboboxSelected>>", self.subject_selected_callback
            )
        # Set sections combobox selection event
        self.comboboxes['section']['widget'].bind(
            "<<ComboboxSelected>>", self.section_selected_callback
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

    
    # AUXILIARY FUNCTIONS
    def intvar_list_to_binary_list(self, intvar_list):
        list = []
        for element in intvar_list:
            list.append(element.get())
        return list

    def get_schedule_dict(self):
        schedule_dictionary = {}
        variable_dictionary = self.parent.children['schedule_child'].schedule_dict
        for day in variable_dictionary:
            schedule_dictionary[day]=self.intvar_list_to_binary_list(variable_dictionary[day])
        return schedule_dictionary

    # CALLBACKS
    def subject_selected_callback(self, ve):
        self.current_subject = self.comboboxes['subject code']['textvariable'].get()
        self.comboboxes['section']['widget']['values']=callbacks.get_section_list(self.current_subject)
        self.comboboxes['section']['textvariable'].set('')
        self.current_section = None
        self.parent.children['schedule_child'].clear_schedule()

        if not (self.current_subject is None) and not (self.current_section is None):
            self.parent.children['schedule_child'].load_schedule(
                self.current_subject, self.current_section)
    
    def section_selected_callback(self, ve):
        self.current_section = self.comboboxes['section']['textvariable'].get()
        self.parent.children['schedule_child'].clear_schedule()
        if not (self.current_subject is None) and not (self.current_section is None):
            self.parent.children['schedule_child'].load_schedule(
                self.current_subject, self.current_section)

    def new_schedule_option(self):
        schedule_dictionary = self.get_schedule_dict()
        subject_code = self.comboboxes['subject code']['textvariable'].get()
        section = self.comboboxes['section']['textvariable'].get()

        validate_result = callbacks.validate_new_schedule_option(subject_code, section)

        if validate_result[0]==subject_code:
            if validate_result[1]==section:
                callbacks.new_schedule_option(subject_code, section, schedule_dictionary)

                self.comboboxes['subject code']['textvariable'].set('')
                self.comboboxes['section']['textvariable'].set('')
                self.current_subject = None
                self.current_section = None
                self.comboboxes['subject code']['widget']['values']=callbacks.get_subject_list()
                self.comboboxes['section']['widget']['values']=callbacks.get_section_list(self.current_subject)

                messagebox.showinfo(
                    title='Agregar opción de horario',
                    message='Horario agragado correctamente'
                )
                self.parent.children['schedule_child'].clear_schedule()
            else:
                messagebox.showinfo(
                    title='Agregar opción de horario',
                    message=validate_result[1]
                )
        elif validate_result[1]==section:
            messagebox.showinfo(
                title='Agregar opción de horario',
                message=validate_result[0]
            )
        else:
            messagebox.showinfo(
                title='Agregar opción de horario',
                message=validate_result[0]+'\n'+validate_result[1]
            )

    def delete_schedule_option(self):
        subject_code = self.comboboxes['subject code']['textvariable'].get()
        section = self.comboboxes['section']['textvariable'].get()
        if not subject_code:
            if not section:
                error_message = 'No hay ramo ni paralelo para eliminar'
            else:
                error_message = 'No hay ramo para eliminar'
            messagebox.showinfo(
                    title='Eliminar opción de horario',
                    message=error_message
                )
        elif not section:
            error_message = 'No hay paralelo para eliminar'
            messagebox.showinfo(
                    title='Eliminar opción de horario',
                    message=error_message
                )
        else:
            anwser = messagebox.askyesno(
                message='¿Estas segur@ de que quieres eliminar el paralelo {} del ramo {}?'.format(section, subject_code),
                title='Eliminar opción de horario'
            )
            if anwser:
                delete_result = callbacks.delete_schedule_option(subject_code, section)
                if type(delete_result)==str:
                    messagebox.showinfo(
                        title='Eliminar opción de horario',
                        message=delete_result
                    )
                self.comboboxes['subject code']['textvariable'].set('')
                self.comboboxes['section']['textvariable'].set('')
                self.current_subject = None
                self.current_section = None

                self.comboboxes['subject code']['widget']['values']=callbacks.get_subject_list()
                self.comboboxes['section']['widget']['values']=callbacks.get_section_list(self.current_subject)
                
            else:
                pass
                
            