from GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.SCHEDULE_FRAME.widgets import Schedule_frame 

schedule_frame = None

def init(parent):
    global schedule_frame
    schedule_frame = Schedule_frame(parent)
    return schedule_frame

def setup():
    global schedule_frame
    schedule_frame.set_widgets()
    schedule_frame.grid()