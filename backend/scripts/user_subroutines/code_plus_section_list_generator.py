def generate_code_plus_section_list(subjects):
    code_plus_section_list = []
    for subject in subjects:
        for section in subject.schedule_options:
            code_plus_section_list.append(subject.code + "_" + str(section))
    return code_plus_section_list