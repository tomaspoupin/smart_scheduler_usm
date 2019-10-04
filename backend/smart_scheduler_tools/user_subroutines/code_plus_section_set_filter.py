#   Module name: code_plus_section_set_filter
#   from package: user_subroutines
#   Used Modules: none
#   Description: generates a set with all possible combinations of subjects,
#   with all possible sections
#   Last Modified: 03/10/2019
#   by: LFC & TAM

#   In: subjects with section list (EX: [DEF101_1, DEF101_2, ...])
#   Out: list of lists of all possible combinations
#   Ex: [[], [DEF101_1], [DEF101_1, DEF102_1], [DEF101_2, DEF102_1], ...]
def compute_power_set(code_list): # Ex: code_list = ["DEF101_1","DEF101_2",...,"DEF10N_M"] 

    if len(code_list) == 0:
        return [[]]
    r = compute_power_set(code_list[:-1])
    return r + [s + [code_list[-1]] for s in r] # [["DEF101_1, DEF101_2,..."],["DEF101_1","DEF102_1",...],...[...]]
                                                # todas las combinaciones, luego filtraremos cuando se repite un ramo c:
# In: List of lists of all possible combinations, length of lists to be filtered
# Out: List of list of length list length with all possible combinations of subjects (with length list length)
# by: LFC & TAM
def filter_set(power_set, list_length):
    filtered_set = []
    for permutation in power_set:
        code_plus_section_list = []
        code_list = []
        if len(permutation) == list_length:
            for element in permutation: 
                if element.split("_")[0] in code_list:
                    break
                code_plus_section_list.append(element)
                code_list.append(element.split("_")[0])
        if len(code_plus_section_list) == list_length:
            filtered_set.append(code_plus_section_list)
    return filtered_set