from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SCHEDULE_FRAME.widgets import Schedule_frame 

def setup(parent):
    schedule_frame = Schedule_frame(parent)
    schedule_frame.set_widgets()
    schedule_frame.grid()
    return schedule_frame.frame