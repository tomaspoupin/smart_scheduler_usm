import structures_subroutines as subroutines

class Schedule:
    'Actual representation of a schedule. formatted as a dictionary'
    days_of_week = ("Mon", "Tue", "Wen", "Thu", "Fri", "Sat")
    def __init__(self):
        self.data = {
        'Mon': [0,0,0,0,0,0,0],
        'Tue': [0,0,0,0,0,0,0],
        'Wen': [0,0,0,0,0,0,0],
        'Thu': [0,0,0,0,0,0,0],
        'Fri': [0,0,0,0,0,0,0],
        'Sat': [0,0,0,0,0,0,0]}

    def change_data(self, day, block, new_state):
        if day in Schedule.days_of_week:
            if new_state == 0 or new_state == 1:
                self.data[day][block] = new_state
    
class Subject:
    'Actual representation of a subject.'
    
    def __init__(self, code, schedule_options):
        self.code = code # Ex: DEF101
        self.schedule_options = schedule_options #tuples list, with each tuple (section, schedule)
        subroutines.sort_schedule_options(self.schedule_options)
    
    def change_schedule_option(self, option):
        option_counter = 0
        for iterable_option in self.schedule_options:
            if iterable_option[0] == option[0]: # index 0 is section
                self.schedule_options[option_counter] = option
                return
            option_counter += 1
        
        self.schedule_options.append(option) # option is a tuple with (section, schedule)
        subroutines.sort_schedule_options(self.schedule_options)