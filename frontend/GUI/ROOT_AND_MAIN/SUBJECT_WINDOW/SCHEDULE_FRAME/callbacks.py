import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# subjects database path
rel_subjects_database_path = "../../../../../database_files/subjects_database.json"
abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)

#READ FUNCTIONS
def load_schedule(subject, section):
    subjects = {}
    try:
        with open(abs_subjects_database_path) as subjects_database:
            subjects = json.load(subjects_database)
    except FileNotFoundError:
        return -2
    except ValueError: #json fails to read
        return -2
    except Exception:
        return -1
    if subject in subjects:
        if section in subjects[subject]:
            return subjects[subject][section]
