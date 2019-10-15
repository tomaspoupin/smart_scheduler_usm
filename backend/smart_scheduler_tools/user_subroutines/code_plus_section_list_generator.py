#   Module name: code_plus_section_list_generator
#   from package: user_subroutines
#   Used Modules: none
#   Description: generates a list with all the subjects with their respective section
#   (Ex: [DEF101_1, DEF101_2 , ..., DEF105_1, DEF105_2, ...])
#   Last Modified: 04/10/2019
#   by: LFC

#   In: subject object list with subscribed subjects
#   Out: A list with all the subjects with sections
#   by: LFC
def generate_code_plus_section_list(subjects):
    code_plus_section_list = []
    for subject in subjects:
        for section in subject.schedule_options:
            code_plus_section_list.append(subject.code + "_" + str(section))
    return code_plus_section_list