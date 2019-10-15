#   Module name: empty_schedule_dict_generator
#   from package: subroutines
#   Used Modules: none
#   Description: generate an empty schedule dict
#   Last Modified: 04/10/2019
#   by: TAM

#   In:
#   Out: an empty schedule dict
def generate_empty_schedule_dict():
    empty_schedule_dict = {
        'Mon': [0,0,0,0,0,0,0],
        'Tue': [0,0,0,0,0,0,0],
        'Wen': [0,0,0,0,0,0,0],
        'Thu': [0,0,0,0,0,0,0],
        'Fri': [0,0,0,0,0,0,0],
        'Sat': [0,0,0,0,0,0,0]}
    return empty_schedule_dict