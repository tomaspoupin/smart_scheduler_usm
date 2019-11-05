import tkinter as tk
from tkinter import ttk

import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SCHEDULE_FRAME.callbacks as callbacks
from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SCHEDULE_FRAME.grid import grid


class Schedule_frame:
    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent.frame)

        self.labels = {
            'block_label': {
                'text': 'Bloques',
                'bg': '#033558',  #siga's blue
                'fg': "white"
            }
        }

        days_dictionary = {'Mon':'Lunes', 'Tue':'Martes', 'Wen':'Miércoles', 
                          'Thu':'Jueves', 'Fri':'Viernes', 'Sat':'Sábado'}
        for day in days_dictionary:
            self.labels[day]={'text':days_dictionary[day],
                              'bg': '#033558',  #siga's blue
                              'fg': "white"}

        blocks_dictionary = {'block1':'1-2', 'block2':'3-4', 'block3':'5-6', 'block4':'7-8',
                             'block5':'9-10', 'block6':'11-12', 'block7':'13-14'}
        for block in blocks_dictionary:
            self.labels[block] = {'text':blocks_dictionary[block],
                                  'bg': '#033558',  #siga's blue
                                  'fg': "white"}

        self.schedule_dict = {
            'Mon': [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
            'Tue': [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
            'Wen': [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
            'Thu': [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
            'Fri': [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()],
            'Sat': [tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()]}

        self.checkboxes = {}

        for day in days_dictionary:
            for block in blocks_dictionary:
                self.checkboxes[day+'_'+block] = {
                    'check_variable':self.schedule_dict[day][int(block[-1])-1] #0
                } 

    def set_widgets(self):
        # set labels
        for label in self.labels:
            self.labels[label]['widget'] = tk.Label(
                self.frame, # parent
                text=self.labels[label]['text'], # text
                bg= self.labels[label]['bg'], # background color
                fg= self.labels[label]['fg'], # text color
                width= 9
            )

        # set checkboxes
        for checkbox in self.checkboxes:
            self.checkboxes[checkbox]['widget'] = tk.Checkbutton(
                self.frame, # parent
                variable = self.checkboxes[checkbox]['check_variable'],
                bg = '#ff9900'
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
    def load_schedule(self, subject, section):
        current_schedule = callbacks.load_schedule(subject, section)
        for day in self.schedule_dict:
            for block_index in range(len(day)):
                self.schedule_dict[day][block_index].set(current_schedule[day][block_index])
    
    def clear_schedule(self):
        for day in self.schedule_dict:
            for block_index in range(len(day)):
                self.schedule_dict[day][block_index].set(0)

