from ROOT_AND_MAIN.widgets import Root_and_main

import ROOT_AND_MAIN.USER_WINDOW.setup as user_window
import ROOT_AND_MAIN.SCHEDULE_WINDOW.setup as schedule_window
import ROOT_AND_MAIN.SUBJECT_WINDOW.setup as subject_window

def setup():
    root_and_main_container = Root_and_main()

    window1 = user_window.setup(root_and_main_container.window_manager)
    window2 = subject_window.setup(root_and_main_container.window_manager)
    window3 = subject_window.setup(root_and_main_container.window_manager)

    root_and_main_container.window_manager.add(window1, text="Usuario")
    root_and_main_container.window_manager.add(window2, text="Ramos")
    root_and_main_container.window_manager.add(window3, text="Horarios")

    root_and_main_container.grid()
    root_and_main_container.run()