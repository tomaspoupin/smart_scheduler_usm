from basic_structures.basic_structures import Schedule

def vector_sum(vector1, vector2):   # It will be used to sum the schedule of each day
    sum_vector = []
    length = len(vector1)
    if len(vector1)==len(vector2):  # It will be 7 in both cases anyways
        for index in range(0, length-1):
            sum_vector.append( vector1[index] + vector2[index] )
    return sum_vector

def schedule_sum(schedule1, schedule2): #schedules are object that represent each schedule. schedule.data is the dictionary itself
    sum_schedule = Schedule()
    if schedule1.data.keys() == schedule2.data.keys():
        for key in schedule1.data.keys():
            sum_schedule.data[key] = vector_sum(schedule1.data[key], schedule2.data[key])
    return sum_schedule
