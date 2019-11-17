import tkinter as tk
from tkinter import ttk

import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.INFO_FRAME.JSON_callbacks as json_callbacks
import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.INFO_FRAME.widget_callbacks as widget_callbacks
from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.INFO_FRAME.grid import grid


class Info_frame:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent.frame)
        self.info_frame = ttk.Frame(self.frame)
        self.title_frame = ttk.Frame(self.frame)
        self.parent = parent
        self.info = {} # dictionary of info with user as key
        self.hide_info = True

        self.labels = {
            'title': {
                'text': '',
                'bg': '#1c95d6'
            },
            'hide info': {
                'text': '> Mostrar Info',
                'bg': '#1c95d6'
            },
            'subjects number': {
                'text': 'Numero de ramos inscritos:',
                'bg': 'white'
            },
            'subject variable': {
                'text': '',
                'bg': 'white'
            },
            'subject table header': {
                'text': 'Ramos inscritos',
                'bg': '#1c95d6'
            },
            'section table header': {
                'text': 'Paralelo',
                'bg': '#1c95d6'
            },
            'overlap table header': {
                'text': 'Topes',
                'bg': '#1c95d6'
            },
            'block table header': {
                'text': 'Bloque',
                'bg': '#1c95d6'
            },
            'day table header': {
                'text': 'Día',
                'bg': '#1c95d6'
            }
        }

    def set_widgets(self):
        # set labels
        for label in self.labels:
            if label == 'title' or label == 'hide info':
                self.labels[label]['widget'] = tk.Label(
                    self.title_frame, # parent
                    text=self.labels[label]['text'], # text
                    bg=self.labels[label]['bg']
                )                
            else:
                self.labels[label]['widget'] = tk.Label(
                    self.info_frame, # parent
                    text=self.labels[label]['text'], # text
                    bg=self.labels[label]['bg']
                )
        self.update_gui_info_to_current_user_option()

        # Events
        self.labels['hide info']['widget'].bind(
            '<Button-1>', self.hide_info_callback
            )
        self.labels['hide info']['widget'].bind(
            '<Enter>', self.hide_info_hover_callback
            )
        self.labels['hide info']['widget'].bind(
            '<Leave>', self.hide_info_leave_callback
            )

    def grid(self):
        self.frame.grid(row=3, column=0)
        self.title_frame.grid(row=0, column=0)
        self.info_frame.grid(row=1, column=0)
        self.info_frame.grid_remove()
        # for widget_type in grid:
        #     for widget_key in grid[widget_type]:
        #         self.__dict__[widget_type][widget_key]['widget'].grid(
        #             row=grid[widget_type][widget_key]["row"],
        #             column=grid[widget_type][widget_key]["column"],
        #             sticky=grid[widget_type][widget_key]["sticky"],
        #             padx=grid[widget_type][widget_key]["padx"],
        #             pady=grid[widget_type][widget_key]["pady"]
        #         )


    # HELPER FUNCTIONS
    def get_current_user(self):
        return self.parent.children['user_child'].current_user

    def get_user_object(self, user_name):
        for user in self.parent.children['user_child'].users:
            if user.get_name() == user_name:
                return user
        return None

    def get_subject_plus_section_list(self, metadata):
        subject_plus_section_list = [] # list of tuples (subject, section)
        for day in metadata:
            for block_index in range(len(metadata[day])):
                if metadata[day][block_index]:
                    for subject_plus_section in metadata[day][block_index].split(' '):
                        subject_plus_section_tuple = tuple(subject_plus_section.split('_'))
                        if subject_plus_section_tuple not in subject_plus_section_list:
                            subject_plus_section_list.append(
                                subject_plus_section_tuple
                            )
        return subject_plus_section_list

    def get_overlaps_dict(self, metadata):
        block_list = ['block1', 'block2', 'block3', 'block4', 'block5', 'block6', 'block7']
        overlaps_dict = {} # dictionary of tuples (subject 1, subject2, ..., subjectn)
        # key is the day + block wich the subjects overlap
        for day in metadata:
            for block_index in range(len(metadata[day])):
                if metadata[day][block_index]:
                    subject_plus_section_list = metadata[day][block_index].split(' ')
                    if len(subject_plus_section_list) > 1:
                        overlaps_dict[day+'_'+block_list[block_index]] = \
                            tuple(subject_plus_section_list)
        return overlaps_dict
                      

    def add_user_to_info_dict(self, user):
        user_object = self.get_user_object(user)
        user_name = user
        self.info[user_name] = {}
        self.info[user_name]['subject_list'] = \
            widget_callbacks.get_subscribed_subjects_list(
                user_name
            )
        if user_object is None:
            return
        
        if not user_object.has_schedule_options():
            return

        schedule_options = user_object.get_schedule_options_as_dict()
        for overlaps in schedule_options:
            self.info[user_name][overlaps] = {}
            for index in range(len(schedule_options[overlaps])):
                option = index + 1
                metadata = user_object.get_option_metadata_as_dict(overlaps, option)
                self.info[user_name][overlaps][option] = {}
                self.info[user_name][overlaps][option]['subject_plus_section_list'] = \
                    self.get_subject_plus_section_list(metadata)
                self.info[user_name][overlaps][option]['overlaps_dict'] = \
                    self.get_overlaps_dict(metadata)

    def get_current_user_info_dict(self):
        user = self.get_current_user()
        if user is None:
            return {}
        if user not in self.info:
            self.add_user_to_info_dict(user)
        return self.info[user]

    def update_user_info(self, user):
        if user not in self.info:
            return
        self.add_user_to_info_dict(user)

    # GUI UPDATE
    # Title frame
    def set_gui_title_frame(self):
        current_user_object = self.get_user_object(self.get_current_user())
        if current_user_object is not None:
            self.labels['title']['text'] = 'INFORMACIÓN DE ' + self.get_current_user().upper()
            self.labels['title']['widget']['text'] = self.labels['title']['text']
        if current_user_object is None:
            self.labels['title']['hide'] = True
            self.labels['hide info']['hide'] = True
        elif current_user_object.has_schedule_options():
            self.labels['title']['hide'] = False
            self.labels['hide info']['hide'] = False
        else:
            self.labels['title']['hide'] = True
            self.labels['hide info']['hide'] = True

    def grid_gui_title_frame(self):
        if self.labels['title']['hide']:
            self.labels['title']['widget'].grid_forget()
            self.labels['hide info']['widget'].grid_forget()
        else:
            self.labels['title']['widget'].grid(
                row=0,
                column=0,
                columnspan=6,
                sticky='wens',
                padx=5,
                pady=5
            )
            self.labels['hide info']['widget'].grid(
                row=0,
                column=6,
                sticky='wens',
                padx=5,
                pady=5
            )

    # INFO FRAME
    def set_subject_number(self, user_info):
        self.labels['subject variable']['text'] = \
            len(user_info['subject_list'])
        self.labels['subject variable']['widget']['text'] = \
            self.labels['subject variable']['text']
        current_user_object = self.get_user_object(self.get_current_user())
        if current_user_object is None:
            self.labels['subjects number']['hide'] = True
            self.labels['subject variable']['hide'] = True        
        elif current_user_object.has_schedule_options():
            self.labels['subjects number']['hide'] = False
            self.labels['subject variable']['hide'] = False
        else:
            self.labels['subjects number']['hide'] = True
            self.labels['subject variable']['hide'] = True

    
    def grid_subject_number(self):
        if self.labels['subjects number']['hide']:
            self.labels['subjects number']['widget'].grid_forget()
            self.labels['subject variable']['widget'].grid_forget()
        else:
            self.labels['subjects number']['widget'].grid(
                row=0,
                column=0,
                columnspan=2,
                sticky='wens',
                padx=5,
                pady=5
            )
            self.labels['subject variable']['widget'].grid(
                row=0,
                column=2,
                sticky='wens',
                padx=5,
                pady=5
            )

    def set_current_user_table_header(self):
        current_user_object = self.get_user_object(self.get_current_user())
        if current_user_object is None:
            self.labels['subject table header']['hide'] = True
            self.labels['section table header']['hide'] = True  
            self.labels['overlap table header']['hide'] = True  
            self.labels['block table header']['hide'] = True   
            self.labels['day table header']['hide'] = True           
        elif current_user_object.has_schedule_options():
            self.labels['subject table header']['hide'] = False
            self.labels['section table header']['hide'] = False
            self.labels['overlap table header']['hide'] = False
            self.labels['block table header']['hide'] = False
            self.labels['day table header']['hide'] = False
        else:
            self.labels['subject table header']['hide'] = True
            self.labels['section table header']['hide'] = True
            self.labels['overlap table header']['hide'] = True  
            self.labels['block table header']['hide'] = True
            self.labels['day table header']['hide'] = True

    def set_current_user_label_table(self, user_info, overlaps, option):
        day_dict = {
            'Mon': 'Lunes',
            'Tue': 'Martes',
            'Wen': 'Miércoles',
            'Thu': 'Jueves',
            'Fri': 'Viernes'
        }
        block_dict = {
            'block1': 'Bloque 1-2',
            'block2': 'Bloque 3-4',
            'block3': 'Bloque 5-6',
            'block4': 'Bloque 7-8',
            'block5': 'Bloque 9-10',
            'block6': 'Bloque 11-12',
            'block7': 'Bloque 13-14',
        }
        # subjects table
        if not user_info:
            return
        row_number = 0
        overlap_number = 0
        if overlaps and option:
            overlaps = int(overlaps)
            option = int(option)
            subject_plus_section_list = \
                user_info[overlaps][option]['subject_plus_section_list']
            subject_plus_section_list.sort()
            overlaps_dict = user_info[overlaps][option]['overlaps_dict']
            row_number = len(subject_plus_section_list)
            for index in range(row_number):
                subject_label_name = 'row_' + str(index) + ':' + 'column_0'
                section_label_name = 'row_' + str(index) + ':' + 'column_1'
                subject, section = subject_plus_section_list[index]
                if subject_label_name not in self.labels:
                    self.labels[subject_label_name] = {}
                    self.labels[subject_label_name]['widget'] = tk.Label(
                        self.info_frame,
                        text='',
                        bg='white'
                    )
                self.labels[subject_label_name]['text'] = subject
                self.labels[subject_label_name]['hide'] = False
                self.labels[subject_label_name]['widget']['text'] = \
                    self.labels[subject_label_name]['text']

                if section_label_name not in self.labels:
                    self.labels[section_label_name] = {}
                    self.labels[section_label_name]['widget'] = tk.Label(
                        self.info_frame,
                        text='',
                        bg='white'
                    )
                self.labels[section_label_name]['text'] = section
                self.labels[section_label_name]['hide'] = False
                self.labels[section_label_name]['widget']['text'] = \
                    self.labels[section_label_name]['text']

            for day_plus_block in overlaps_dict:
                day, block = day_plus_block.split('_')
                overlaped_subjects_tuple = overlaps_dict[day_plus_block]
                overlap_label_name = 'overlap_' + str(overlap_number)
                day_label_name = 'day_' + str(overlap_number)
                block_label_name = 'block_' + str(overlap_number)

                if overlap_label_name not in self.labels:
                    self.labels[overlap_label_name] = {}
                    self.labels[overlap_label_name]['widget'] = tk.Label(
                        self.info_frame, text='', bg='white'
                    )
                overlap_str = ''
                for overlaped_subject in overlaped_subjects_tuple:
                    overlap_str = overlap_str + overlaped_subject.split('_')[0] + ', '
                overlap_str = overlap_str[:-2]
                self.labels[overlap_label_name]['text'] = overlap_str
                self.labels[overlap_label_name]['hide'] = False
                self.labels[overlap_label_name]['widget']['text'] = \
                    self.labels[overlap_label_name]['text']

                if day_label_name not in self.labels:
                    self.labels[day_label_name] = {}
                    self.labels[day_label_name]['widget'] = tk.Label(
                        self.info_frame, text='', bg='white'
                    )
                self.labels[day_label_name]['text'] = day_dict[day]
                self.labels[day_label_name]['hide'] = False
                self.labels[day_label_name]['widget']['text'] = \
                    self.labels[day_label_name]['text']

                if block_label_name not in self.labels:
                    self.labels[block_label_name] = {}
                    self.labels[block_label_name]['widget'] = tk.Label(
                        self.info_frame, text='', bg='white'
                    )
                self.labels[block_label_name]['text'] = block_dict[block]
                self.labels[block_label_name]['hide'] = False
                self.labels[block_label_name]['widget']['text'] = \
                    self.labels[block_label_name]['text']
                overlap_number += 1
                
            # Hide every label not in the user table
        while True:
            subject_label_name = 'row_' + str(row_number) + ':' + 'column_0'
            section_label_name = 'row_' + str(row_number) + ':' + 'column_1'
            if subject_label_name in self.labels:
                self.labels[subject_label_name]['hide'] = True
                self.labels[section_label_name]['hide'] = True
                row_number += 1
            else:
                break

        while True:
            overlap_label_name = 'overlap_' + str(overlap_number)
            day_label_name = 'day_' + str(overlap_number)
            block_label_name = 'block_' + str(overlap_number)
            if overlap_label_name in self.labels:
                self.labels[overlap_label_name]['hide'] = True
                self.labels[day_label_name]['hide'] = True
                self.labels[block_label_name]['hide'] = True
                overlap_number += 1
            else:
                break

    def grid_current_user_label_table(self):
        # table header
        if self.labels['subject table header']['hide']:
            self.labels['subject table header']['widget'].grid_forget()
            self.labels['section table header']['widget'].grid_forget()
        else:
            self.labels['subject table header']['widget'].grid(
                row=1,
                column=0,
                columnspan=2,
                sticky='wens',
                padx=5,
                pady=5
            )
            self.labels['section table header']['widget'].grid(
                row=1,
                column=2,
                sticky='wens',
                padx=5,
                pady=5
            )
        # table info
        visible_row_number = 0
        row_number = 0
        overlap_number = 0
        while True:
            subject_label_name = 'row_' + str(row_number) + ':' + 'column_0'
            section_label_name = 'row_' + str(row_number) + ':' + 'column_1'
            if subject_label_name in self.labels:
                if not self.labels[subject_label_name]['hide']:
                    self.labels[subject_label_name]['widget'].grid(
                        row=row_number+2,
                        column=0,
                        columnspan=2,
                        sticky='wens',
                        padx=5,
                        pady=5
                    )
                    self.labels[section_label_name]['widget'].grid(
                        row=row_number+2,
                        column=2,
                        sticky='wens',
                        padx=5,
                        pady=5
                    )
                    visible_row_number += 1
                else:
                    self.labels[subject_label_name]['widget'].grid_forget()
                    self.labels[section_label_name]['widget'].grid_forget()
                row_number += 1
            else:
                break
        if self.labels['overlap table header']['hide']:
            self.labels['overlap table header']['widget'].grid_forget()
            self.labels['block table header']['widget'].grid_forget()
        else:
            self.labels['overlap table header']['widget'].grid(
                row=visible_row_number+2,
                column=0,
                sticky='wens',
                padx=5,
                pady=5
            )
            self.labels['block table header']['widget'].grid(
                row=visible_row_number+2,
                column=2,
                sticky='wens',
                padx=5,
                pady=5
            )
            self.labels['day table header']['widget'].grid(
                row=row_number+2,
                column=1,
                sticky='wens',
                padx=5,
                pady=5
            )

        while True:
            overlap_label_name = 'overlap_' + str(overlap_number)
            day_label_name = 'day_' + str(overlap_number)
            block_label_name = 'block_' + str(overlap_number)
            if overlap_label_name in self.labels:
                if not self.labels[overlap_label_name]['hide']:
                    self.labels[overlap_label_name]['widget'].grid(
                        row=visible_row_number+3,
                        column=0,
                        sticky='wens',
                        padx=5,
                        pady=5
                    )
                    self.labels[day_label_name]['widget'].grid(
                        row=visible_row_number+3,
                        column=1,
                        sticky='wens',
                        padx=5,
                        pady=5
                    )
                    self.labels[block_label_name]['widget'].grid(
                        row=visible_row_number+3,
                        column=2,
                        sticky='wens',
                        padx=5,
                        pady=5
                    )
                    visible_row_number += 1
                else:
                    self.labels[overlap_label_name]['widget'].grid_forget()
                    self.labels[day_label_name]['widget'].grid_forget()
                    self.labels[block_label_name]['widget'].grid_forget()
                overlap_number += 1
            else:
                break

    def set_gui_info_frame(self):
        user_info = self.get_current_user_info_dict()
        if not user_info:
            return
        overlaps = \
            self.parent.children['selection_child'].comboboxes['overlaps']['textvariable'].get()
        option = \
            self.parent.children['selection_child'].comboboxes['options']['textvariable'].get()
        self.set_subject_number(user_info)
        self.set_current_user_table_header()
        self.set_current_user_label_table(user_info, overlaps, option)

    def grid_gui_info_frame(self):
        if self.get_current_user() is None:
            return
        self.grid_subject_number()
        self.grid_current_user_label_table()

    def update_gui_info_to_current_user_option(self):
        self.set_gui_title_frame()
        self.set_gui_info_frame()
        self.grid_gui_title_frame()
        self.grid_gui_info_frame()

    # CALLBACKS
    def hide_info_callback(self, ve):
        self.change_info_frame_visibility()
        
    def change_info_frame_visibility(self):
        if self.hide_info:
            self.labels['hide info']['text'] = 'v Ocultar Info'
            self.labels['hide info']['widget']['text'] = \
                self.labels['hide info']['text']
            self.info_frame.grid()
            self.hide_info = False
        else:
            self.labels['hide info']['text'] = '> Mostrar Info'
            self.labels['hide info']['widget']['text'] = \
                self.labels['hide info']['text']
            self.info_frame.grid_remove()
            self.hide_info = True

    def hide_info_hover_callback(self, ve):
        self.labels['hide info']['widget']['bg'] = "#ff9900"

    def hide_info_leave_callback(self, ve):
        self.labels['hide info']['widget']['bg'] = '#1c95d6'