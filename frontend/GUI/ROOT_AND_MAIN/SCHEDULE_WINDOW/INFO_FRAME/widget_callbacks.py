import GUI.ROOT_AND_MAIN.SCHEDULE_WINDOW.INFO_FRAME.JSON_callbacks as json

def get_subscribed_subjects_list(user):
    if user is None:
        return 0
    subject_list = json.get_user_subjects_list(user)
    return subject_list