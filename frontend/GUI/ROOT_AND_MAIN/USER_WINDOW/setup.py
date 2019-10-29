from GUI.ROOT_AND_MAIN.USER_WINDOW.widgets import User_window

import GUI.ROOT_AND_MAIN.USER_WINDOW.USER_FRAME.setup as user_frame
import GUI.ROOT_AND_MAIN.USER_WINDOW.SUBJECT_FRAME.setup as subject_frame

def setup(parent):
    user_window = User_window(parent)

    user_frame.setup(user_window.window)
    subject_frame.setup(user_window.window)

    user_window.grid()

    return user_window.window