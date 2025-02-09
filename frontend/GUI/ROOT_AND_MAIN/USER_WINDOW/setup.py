from GUI.ROOT_AND_MAIN.USER_WINDOW.widgets import User_window

import GUI.ROOT_AND_MAIN.USER_WINDOW.USER_FRAME.setup as user_frame
import GUI.ROOT_AND_MAIN.USER_WINDOW.SUBJECT_FRAME.setup as subject_frame

def setup(parent):
    user_window = User_window(parent)
    user_window.add_children(
        user_child=user_frame.init(user_window),
        subject_child=subject_frame.init(user_window)
    )
    user_frame.setup()
    subject_frame.setup()

    user_window.grid()

    return user_window