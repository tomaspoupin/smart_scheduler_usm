import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
rel_users_database_path = "../../../../../database_files/users_database.json"
abs_users_database_path = os.path.join(BASE_DIR, rel_users_database_path)

def validate_user(user_name):
    if not user_name:
        return ('Error: Ingrese usuario',)
    if len(user_name.split()) != 1:
        return ('Error: No se admiten más de una palabra',)
    if len(user_name) > 20:
        return ('Error: Máximo 20 caracteres',)
    return user_name

def add_new_user(user_name):
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

    # then we add the new user
    users[user_name] = {
        'subjects': [],
        'schedule options': {}
    }
    try:
        with open(abs_users_database_path, 'w') as users_database:
            json.dump(users, users_database, sort_keys=True, indent=4)
    except Exception:
        return -1
    return 1

def remove_user(user_name):
    users = {}
    try:
        with open(abs_users_database_path) as users_database:
            users = json.load(users_database)
    except FileNotFoundError:
        return -2
    except Exception:
        return -1
    # Remove the key
    success = users.pop(user_name, None)
    if success is None:
        return -2 # Means that database is not in sync with GUI
    # Write back to database
    try:
        with open(abs_users_database_path, 'w') as users_database:
            json.dump(users, users_database, sort_keys=True, indent=4)
    except Exception:
        return -1
    return 1

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