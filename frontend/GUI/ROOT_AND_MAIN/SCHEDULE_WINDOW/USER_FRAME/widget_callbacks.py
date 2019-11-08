import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.USER_FRAME.JSON_callbacks as json_callbacks

def calculate_schedule_options(user):
    user.clear_subjects()
    user.clear_schedule_options()
    subjects = json_callbacks.get_user_subjects_list(user.get_name())
    if not subjects:
        pass
    else:
        for subject in subjects:
            user.load_subject_from_json(subject)
    user.compute_possible_schedules()