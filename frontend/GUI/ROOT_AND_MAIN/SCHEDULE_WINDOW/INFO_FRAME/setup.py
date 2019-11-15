from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.INFO_FRAME.widgets import Info_frame 

info_frame = None

def init(parent):
    global info_frame
    info_frame = Info_frame(parent)
    return info_frame

def setup():
    global info_frame
    info_frame.set_widgets()
    info_frame.grid()