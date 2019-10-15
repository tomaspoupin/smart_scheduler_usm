from ROOT_AND_MAIN.USER_WINDOW.USER_FRAME.widgets import User_frame

def setup(parent):
    user_frame = User_frame(parent)
    user_frame.set_widgets()
    user_frame.grid()
    return user_frame.frame