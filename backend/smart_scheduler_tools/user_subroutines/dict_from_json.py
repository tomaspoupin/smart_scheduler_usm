#   Module name: dict_from_json
#   from package: user_subroutines
#   Used Modules: os, json
#   Description: Load all the subjects from a json file and retruns it as a dict
#   Last Modified: 04/10/2019
#   by: TAM

import os
import json

# In:
# Out: A dictionary containing subjects as a dictionary.
# Ex: 
    # {
  	# "DEF105":
	# {
	# "1":
	# 	{
    # 	"Mon": [0,0,0,0,0,0,0],
    # 	"Tue": [0,1,0,0,0,0,0],
    # 	"Wen": [0,0,0,0,0,0,0],
    # 	"Thu": [0,0,0,0,0,0,0],
    # 	"Fri": [0,1,0,0,1,1,0],
    # 	"Sat": [0,0,0,0,0,0,0]
	# 	},
	# "2":
    # 	{
    # 	"Mon": [0,0,0,0,0,0,0],
    #     "Tue": [0,0,0,0,0,0,0],
    #     "Wen": [0,0,0,0,0,0,0],
    #     "Thu": [0,0,0,1,1,0,0],
    #     "Fri": [0,0,0,0,1,1,0],
    #     "Sat": [0,0,0,0,0,0,0]
    # 	}
    # },
    # ...
    # "DEF102":
    # {
    # ...
    # }
    # }
#   by: TAM
def get_dict_from_json_subject_database():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    rel_subjects_database_path = "../../../database_files/subjects_database.json"
    abs_subjects_database_path = os.path.join(BASE_DIR, rel_subjects_database_path)
    try:
        with open(abs_subjects_database_path, "r") as json_file:
            json_dict = json.load(json_file)
            return json_dict
    except: # if something goes wrong returns an empty dict
            return {}