from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.widgets import Subject_window

import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SCHEDULE_FRAME.setup as schedule_frame
import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.setup as subject_frame

def setup(parent):
    subject_window = Subject_window(parent)

    schedule_frame.setup(subject_window.window)
    subject_frame.setup(subject_window.window)   

    subject_window.grid()

    return subject_window.window