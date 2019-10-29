from GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.widgets import Schedule_window

import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.setup as user_frame
import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.SELECTION_FRAME.setup as selection_frame
import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.SCHEDULE_FRAME.setup as schedule_frame

def setup(parent):
    schedule_window = Schedule_window(parent)

    user_frame.setup(schedule_window.window)
    selection_frame.setup(schedule_window.window)
    schedule_frame.setup(schedule_window.window)
    
    schedule_window.grid()

    return schedule_window.window