#   Module name: subject_list_to_dictionary
#   from package: user_subroutines
#   Used Modules: none
#   Description: transforms a subject list to a subject dictionary
#   Last Modified: 04/10/2019
#   by: TAM & LFC

#   In: subjects list
#   Out: subjects dictionary
#   by: LFC & TAM
def subject_list_to_dict(subject_list):
    subject_dict = {}
    for subject in subject_list:
        subject_dict[subject.code] = subject.schedule_options
    return subject_dict