#   Module name: vector_sum
#   from package: subroutines
#   Used Modules: none
#   Description: given two vectors (list or tuples), return the sum of both vectors
#   Last Modified: 04/10/2019
#   by: LFC

#   In: Two vectors to be added to each other
#   Out: a list/tuple with the sum of both vectors
#   by: LFC
def vector_sum(vector1, vector2):   # It will be used to sum the schedule of each day
    sum_vector = []
    length = len(vector1)
    if len(vector1)==len(vector2):  # It will be 7 in both cases anyways
        for index in range(length):
            sum_vector.append( vector1[index] + vector2[index] )
    return sum_vector