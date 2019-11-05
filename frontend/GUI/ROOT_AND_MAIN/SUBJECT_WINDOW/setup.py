from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.widgets import Subject_window

import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SCHEDULE_FRAME.setup as schedule_frame
import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.setup as subject_frame

def setup(parent):
    subject_window = Subject_window(parent)
    subject_window.add_children(
        schedule_child=schedule_frame.init(subject_window),
        subject_child=subject_frame.init(subject_window)
    )
    schedule_frame.setup()
    subject_frame.setup()

    subject_window.grid()

    return subject_window