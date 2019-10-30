#!usr/bin/env python
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# packages path
rel_gui_path = "../frontend/"
abs_gui_path = os.path.join(BASE_DIR, rel_gui_path)
rel_smart_scheduler_tools_path = "../backend/"
abs_smart_scheduler_tools_path = os.path.join(BASE_DIR, rel_smart_scheduler_tools_path)

# database path
rel_subjects_database_path = "../database_files/subjects_database.json"
abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)
rel_users_database_path = "../database_files/users_database.json"
abs_users_database_path = os.path.join(BASE_DIR, rel_users_database_path)

# create databases if not exist
try:
    open(abs_subjects_database_path, 'a').close()
    open(abs_users_database_path, 'a').close()
except:
    raise Exception()

if os.stat(abs_subjects_database_path).st_size == 0:
    try:
        with open(abs_subjects_database_path, 'w') as file:
            file.write('{}')
    except:
        raise Exception()
if os.stat(abs_users_database_path).st_size == 0:
    try:
        with open(abs_users_database_path, 'w') as file:
            file.write('{}')
    except:
        raise Exception()

# Add packages
sys.path.append(abs_gui_path)
sys.path.append(abs_smart_scheduler_tools_path)

import GUI

GUI.run()