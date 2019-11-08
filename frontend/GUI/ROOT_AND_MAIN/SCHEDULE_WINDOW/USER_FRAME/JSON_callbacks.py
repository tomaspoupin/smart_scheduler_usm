import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# subjects database path
rel_subjects_database_path = "../../../../../database_files/subjects_database.json"
abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)

# users database path
rel_users_database_path = "../../../../../database_files/users_database.json"
abs_users_database_path = os.path.join(BASE_DIR, rel_users_database_path)

# READ FUNCTIONS
def get_user_list():
    users = {}
    try:
        with open(abs_users_database_path) as users_database:
            users = json.load(users_database)
    except FileNotFoundError:
        return -2
    except ValueError:
        return -2
    except:
        return -1
    return list(users.keys())

def get_user_subjects_list(user):
    users = {}
    try:
        with open(abs_users_database_path) as users_database:
            users = json.load(users_database)
    except FileNotFoundError:
        return -2
    except ValueError:
        return -2
    except:
        return -1
    return users[user]['subjects']