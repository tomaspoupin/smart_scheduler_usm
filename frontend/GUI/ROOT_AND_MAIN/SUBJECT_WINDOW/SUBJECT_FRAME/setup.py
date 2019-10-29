from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.widgets import Subject_frame

def setup(parent):
    subject_frame = Subject_frame(parent)
    subject_frame.set_widgets()
    subject_frame.grid()
    return subject_frame.frame