from GUI.ROOT_AND_MAIN.widgets import Root_and_main

import GUI.ROOT_AND_MAIN.USER_WINDOW.setup as user_window
import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.setup as schedule_window
import GUI.ROOT_AND_MAIN.SUBJECT_WINDOW.setup as subject_window

root_and_main_container = Root_and_main()

def setup():
    global root_and_main_container

    window1 = user_window.setup(root_and_main_container.window_manager)
    window2 = subject_window.setup(root_and_main_container.window_manager)
    window3 = schedule_window.setup(root_and_main_container.window_manager)

    root_and_main_container.window_manager.add(window1.frame, text="Usuario")
    root_and_main_container.window_manager.add(window2, text="Ramos")
    root_and_main_container.window_manager.add(window3, text="Horarios")

    root_and_main_container.grid()

def run():
    global root_and_main_container
    root_and_main_container.run()