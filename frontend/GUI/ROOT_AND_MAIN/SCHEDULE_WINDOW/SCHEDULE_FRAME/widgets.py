import tkinter as tk
from tkinter import ttk

import ROOT_AND_MAIN.SCHEDULE_WINDOW.SCHEDULE_FRAME.callbacks as callbacks
from ROOT_AND_MAIN.SCHEDULE_WINDOW.SCHEDULE_FRAME.grid import grid


class Schedule_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        
        # siga's orange => #ff9900
        self.labels = {
            'block_label': {
                'text': 'Bloques',
                'bg': '#033558',  #siga's blue
                'fg': "white"
            }
        }

        days_dictionary = {'monday':'Lunes', 'tuesday':'Martes', 'wednesday':'Miércioles', 
                          'thursday':'Jueves', 'friday':'Viernes', 'saturday':'Sábado'}
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


    def set_widgets(self):
        # set labels
        for label in self.labels:
            self.labels[label]['widget'] = tk.Label(
                self.frame, # parent
                text= self.labels[label]['text'], # text
                bg= self.labels[label]['bg'], # background color
                fg= self.labels[label]['fg'], # text color
                width= 9
            )


    def grid(self):
        self.frame.grid(row=2, column=0)

        for widget_type in grid:
            for widget_key in grid[widget_type]:
                self.__dict__[widget_type][widget_key]['widget'].grid(
                    row=grid[widget_type][widget_key]["row"],
                    column=grid[widget_type][widget_key]["column"],
                    sticky=grid[widget_type][widget_key]["sticky"],
                    padx=grid[widget_type][widget_key]["padx"],
                    pady=grid[widget_type][widget_key]["pady"]
                )
