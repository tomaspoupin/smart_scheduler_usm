from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.widgets import User_frame 

user_frame = None

def init(parent):
    global user_frame
    user_frame = User_frame(parent)
    return user_frame

def setup():
    global user_frame
    user_frame.set_widgets()
    user_frame.grid()