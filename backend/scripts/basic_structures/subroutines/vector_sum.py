def vector_sum(vector1, vector2):   # It will be used to sum the schedule of each day
    sum_vector = []
    length = len(vector1)
    if len(vector1)==len(vector2):  # It will be 7 in both cases anyways
        for index in range(length):
            sum_vector.append( vector1[index] + vector2[index] )
    return sum_vector