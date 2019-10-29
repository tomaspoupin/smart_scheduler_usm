#!usr/bin/env python
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
rel_gui_path = "../frontend/"
abs_gui_path = os.path.join(BASE_DIR, rel_gui_path)
rel_smart_scheduler_tools_path = "../backend/"
abs_smart_scheduler_tools_path = os.path.join(BASE_DIR, rel_smart_scheduler_tools_path)

sys.path.append(abs_gui_path)
sys.path.append(abs_smart_scheduler_tools_path)

import GUI

GUI.run()