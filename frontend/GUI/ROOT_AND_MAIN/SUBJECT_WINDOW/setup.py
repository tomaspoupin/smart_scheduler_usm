from ROOT_AND_MAIN.SUBJECT_WINDOW.widgets import Subject_window

def setup(parent):
    subject_window = Subject_window(parent)
    subject_window.grid()
    return subject_window.window