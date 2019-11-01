import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# subjects database path
rel_subjects_database_path = "../../../../../database_files/subjects_database.json"
abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)

# users database path
rel_users_database_path = "../../../../../database_files/users_database.json"
abs_users_database_path = os.path.join(BASE_DIR, rel_users_database_path)

def subscribe_subject(user, subject):
    users = {}
    try:
        with open(abs_users_database_path) as users_database:
            users = json.load(users_database)
    except FileNotFoundError:
        return -2
    except ValueError: #json fails to read
        return -2
    except Exception:
        return -1

    users[user]['subjects'].append(subject)
    users[user]['subjects'].sort()

    try:
        with open(abs_users_database_path, 'w') as users_database:
            json.dump(users, users_database, sort_keys=True, indent=4)
    except Exception:
        return -1
    return 1

def unsubscribe_subject(user, subject):
    users = {}
    try:
        with open(abs_users_database_path) as users_database:
            users = json.load(users_database)
    except FileNotFoundError:
        return -2
    except ValueError: #json fails to read
        return -2
    except Exception:
        return -1

    # Remove the subject
    if subject not in users[user]['subjects']:
        return -2 # Means that database is not in sync with GUI

    users[user]['subjects'].remove(subject)
    users[user]['subjects'].sort()
    # Write back to database
    try:
        with open(abs_users_database_path, 'w') as users_database:
            json.dump(users, users_database, sort_keys=True, indent=4)
    except Exception:
        return -1
    return 1

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