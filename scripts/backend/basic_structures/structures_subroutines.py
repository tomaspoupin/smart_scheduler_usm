def sort_schedule_options(schedule_options):
    length = len(schedule_options)
    for i in range(length):
        for j in range(0, length-i-1):
            if schedule_options[j][0] > schedule_options[j+1][0] :
                schedule_options[j], schedule_options[j+1] = schedule_options[j+1], schedule_options[j]