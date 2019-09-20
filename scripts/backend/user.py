import basic_structures.basic_structures as structure

class User:
    'User who contains info about wanted subjects.'
    def __init__(self, name, subjects=[]):
        self.name = name
        self.subjects = subjects
        self.schedule_options = {0: [], 1: [], 2: [], 3: []} # the keys are the number of overlaps in the possible schedules
    
    def change_subjects(self, code, new_state):
        subject_counter = 0
        for iterable_code in self.subjects:
            if iterable_code == code:
                if new_state == 0: # remove the subject
                    self.subjects.pop(subject_counter)
                    return
                else:
                    return
            subject_counter += 1
        if new_state == 1: # add the subject
            self.subjects.append(code)