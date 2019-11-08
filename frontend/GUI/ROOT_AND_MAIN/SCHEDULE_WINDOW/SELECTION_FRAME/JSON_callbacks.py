import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# subjects database path
rel_subjects_database_path = "../../../../../database_files/subjects_database.json"
abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)

# users database path
rel_users_database_path = "../../../../../database_files/users_database.json"
abs_users_database_path = os.path.join(BASE_DIR, rel_users_database_path)

# READ FUNCTION