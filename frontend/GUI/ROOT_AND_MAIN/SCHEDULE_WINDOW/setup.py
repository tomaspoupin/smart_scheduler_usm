from ROOT_AND_MAIN.SCHEDULE_WINDOW.widgets import Schedule_window

def setup(parent):
    schedule_window = Schedule_window(parent)
    schedule_window.grid()
    return schedule_window.window