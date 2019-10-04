#   Module name: user
#   from package: smart_scheduler_tools
#   Used Modules: basic_structures_definitions, code_plus_section_list_generator,
#   code_plus_section_set_filter, subject_list_to_dictionary, dict_from_json
#   Description: Its the most fundamental class of the application, it uses all the
#   basic structures and it stores the user info, this info includes: Subribed subjects,
#   name, posible schedules.
#   Last Modified: 03/10/2019
#   by: LFC & TAM

from smart_scheduler_tools.basic_structures.basic_structures_definitions import Schedule
from smart_scheduler_tools.basic_structures.basic_structures_definitions import Subject
from smart_scheduler_tools.user_subroutines.code_plus_section_list_generator import generate_code_plus_section_list
from smart_scheduler_tools.user_subroutines.code_plus_section_set_filter import *
from smart_scheduler_tools.user_subroutines.subject_list_to_dictionary import subject_list_to_dict
from smart_scheduler_tools.user_subroutines.dict_from_json import get_dict_from_json_subject_database

class User:
    'User who contains info about wanted subjects.'
    def __init__(self, name, subjects=[]):
        self.name = name
        self.subjects = subjects # subject's list
        self.schedule_options = {} # the keys are the number of overlaps in the possible schedules
    
    # In: self user, subject object, add/remove flag
    # Out: the self.subjects list is updated
    # by LFC & TAM
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

    # In: self user, subject code (Ex: DEF101)
    # Out: it stores in self.subjects list the subject taken from
    # the subjects database
    # by LFC & TAM
    def load_subject_from_json(self, code):
        subjects_database = get_dict_from_json_subject_database()
        new_schedule_options = {}
        if code in subjects_database:
            # check if the subject is within the subject list to replace it
            for i in range(len(self.subjects)):
                if self.subjects[i].code == code:
                    self.subjects.pop(i)
            # then we add the new subject
            for section in subjects_database[code]:
                new_schedule_options[int(section)] = Schedule(subjects_database[code][section])
        else:
            return
        new_subject = Subject(code, new_schedule_options)
        self.subjects.append(new_subject)

    # In: self user
    # Out: fills the self.schedule_options dictionary with possible schedules, organized
    # by the amount of overlaps (the keys of the dictionary are the overlaps)
    # by LFC & TAM
    def compute_possible_schedules(self):
        code_plus_section_list = generate_code_plus_section_list(self.subjects)
        power_set = compute_power_set(code_plus_section_list)
        filtered_set = filter_set(power_set, len(self.subjects))

        subject_as_dict = subject_list_to_dict(self.subjects)

        possible_schedule = Schedule()
        for subject_combination in filtered_set:
            
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
            possible_schedule.clear()