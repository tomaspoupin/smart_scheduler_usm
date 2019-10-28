from ROOT_AND_MAIN.SCHEDULE_WINDOW.SELECTION_FRAME.widgets import Selection_frame

def setup(parent):
    selection_frame = Selection_frame(parent)
    selection_frame.set_widgets()
    selection_frame.grid()
    return selection_frame.frame