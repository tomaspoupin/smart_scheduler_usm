import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# subjects database path
rel_subjects_database_path = "../../../../../database_files/subjects_database.json"
abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)

# users database path
rel_users_database_path = "../../../../../database_files/users_database.json"
abs_users_database_path = os.path.join(BASE_DIR, rel_users_database_path)

def subscribe_subject(stringvar):
    pass

def unsubscribe_subject(stringvar):
    pass

def get_possible_subjects_list():
    subjects = {}
    try:
        with open(abs_subjects_database_path) as subjects_database:
            subjects = json.load(subjects_database)
    except FileNotFoundError:
        return -2
    except ValueError:
        return -2
    except:
        return -1
    return list(subjects.keys())