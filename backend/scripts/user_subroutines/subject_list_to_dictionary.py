def subject_list_to_dict(subject_list):
    subject_dict = {}
    for subject in subject_list:
        subject_dict[subject.code] = subject.schedule_options
    return subject_dict