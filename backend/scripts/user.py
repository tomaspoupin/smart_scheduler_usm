import os
import json

from basic_structures.basic_structures_script import Schedule
from basic_structures.basic_structures_script import Subject
from user_subroutines.code_plus_section_list_generator import generate_code_plus_section_list
from user_subroutines.code_plus_section_set_filter import *
from user_subroutines.subject_list_to_dictionary import subject_list_to_dict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class User:
    'User who contains info about wanted subjects.'
    def __init__(self, name, subjects=[]):
        self.name = name
        self.subjects = subjects # subject's list
        self.schedule_options = {0: [], 1: [], 2: [], 3: []} # the keys are the number of overlaps in the possible schedules
    
    def change_subjects(self, subject, new_state):
        length = len(self.subjects)
        for i in range(length):
            if self.subjects[i].code == subject.code:
                if new_state == 0: # remove the subject
                    self.subjects.pop(i)
                elif new_state == 1:
                    self.subjects[i] = subject
                return
        if new_state == 1: # add the subject
            self.subjects.append(subject)

    def load_subject_from_json(self, code):
        rel_subjects_database_path = "../../database_files/subjects_database.json"
        abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)
        subjects_database = {}
        try:
            with open(abs_subjects_database_path, "r") as json_file:
                subjects_database = json.load(json_file)
        except:
            return

        subject_counter = 0 # check if the subject is within the subject list
        for iterable_subject in self.subjects:
            if iterable_subject.code == code:
                self.subjects.pop(subject_counter)
            subject_counter += 1

        new_schedule_options = {}
        if code in subjects_database:
            for section in subjects_database[code]:
                new_schedule_options[int(section)] = Schedule(subjects_database[code][section])
        else:
            return
        new_subject = Subject(code, new_schedule_options)
        self.subjects.append(new_subject)

    def compute_possible_schedules(self):
        code_plus_section_list = generate_code_plus_section_list(self.subjects)
        power_set = compute_power_set(code_plus_section_list)
        filtered_set = filter_set(power_set, len(self.subjects))

        subject_as_dict = subject_list_to_dict(self.subjects)

        possible_schedule = Schedule()
        for subject_combination in filtered_set:
            possible_schedule.clear()
            
            for code_plus_section in subject_combination:
                [code, section] = code_plus_section.split("_")
                schedule_to_add = subject_as_dict[code][int(section)]
                possible_schedule.add_schedule(schedule_to_add)
            
            possible_schedule.compute_overlaps()
            new_schedule = Schedule(possible_schedule.data)       
            if possible_schedule.overlaps in self.schedule_options:
                self.schedule_options[possible_schedule.overlaps].append(new_schedule)
            else:
                self.schedule_options[possible_schedule.overlaps] = [new_schedule]