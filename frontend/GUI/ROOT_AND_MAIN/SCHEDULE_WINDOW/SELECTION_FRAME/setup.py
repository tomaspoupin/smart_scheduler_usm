from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.SELECTION_FRAME.widgets import Selection_frame

selection_frame = None

def init(parent):
    global selection_frame
    selection_frame = Selection_frame(parent)
    return selection_frame

def setup():
    global selection_frame
    selection_frame.set_widgets()
    selection_frame.grid()