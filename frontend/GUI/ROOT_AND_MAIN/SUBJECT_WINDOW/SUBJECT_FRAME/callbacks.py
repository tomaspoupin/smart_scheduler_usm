import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# subjects database path
rel_subjects_database_path = "../../../../../database_files/subjects_database.json"
abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)

#WRITE FUNCTIONS-------------------------------------------------------------------
def new_schedule_option(subject_code, section, schedule_dictionary):
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

    if subject_code in subjects:
        subjects[subject_code][section] = schedule_dictionary
    else:
        subjects[subject_code]={}
        subjects[subject_code][section] = schedule_dictionary

    try:
        with open(abs_subjects_database_path, 'w') as subjects_database:
            json.dump(subjects, subjects_database, sort_keys=False, indent=4)
    except Exception:
        return -1
    return 1

def delete_schedule_option(subject_code, section):
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


    if subject_code in subjects:
        if section in subjects[subject_code]:
            subjects[subject_code].pop(section)
            if len(subjects[subject_code])==0:
                subjects.pop(subject_code)
        else:
            print('Error: no existe el paralelo indicado')
            return 'Error: no existe el paralelo indicado'
    else:
        print('Error: no existe el ramo indicado')
        return 'Error: no existe el ramo indicado'

    try:
        with open(abs_subjects_database_path, 'w') as subjects_database:
            json.dump(subjects, subjects_database, sort_keys=False, indent=4)
    except Exception:
        return -1
    print('El paralelo {} del ramo {} fue eliminado correctamente'.format(section, subject_code))
    return ('El paralelo {} del ramo {} fue eliminado correctamente'.format(section, subject_code))

#READ FUNCTIONS---------------------------------------------------------------
def get_subject_list():
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
    return list(subjects.keys())

def get_section_list(current_subject):
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
    if current_subject is None:
        return []
    return list(subjects[current_subject].keys())
    
#AUX FUNCTIONS--------------------------------------------------------------------
def validate_new_schedule_option(subject, section):
    if len(subject)==6:
        alpha = subject[0]+subject[1]+subject[2]
        num = subject[3]+subject[4]+subject[5]
    else:
        alpha = ''
        num = ''
    subject_response = subject
    section_response = section
    if not subject:
        subject_response = 'Error: Ingrese ramo'
    elif len(subject.split())!= 1 or len(subject)!=6 or (not alpha.isalpha()) or (not num.isdigit()):
        subject_response = 'Error formato ramo. Ejemplo correcto: DEF101'
    if not section:
        section_response = 'Error: Ingrese paralelo'
    elif (not section.isdigit()) or int(section)>9:
        section_response = 'Error: paralelo debe ser un número menor que 10'
    return (subject_response, section_response)