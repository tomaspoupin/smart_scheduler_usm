from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SUBJECT_FRAME.widgets import Subject_frame

subject_frame = None

def init(parent):
    global subject_frame
    subject_frame = Subject_frame(parent)
    return subject_frame

def setup():
    global subject_frame
    subject_frame.set_widgets()
    subject_frame.grid()