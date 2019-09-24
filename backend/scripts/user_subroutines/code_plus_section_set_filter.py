def compute_power_set(code_list): # Ex: code_list = ["DEF101_1","DEF101_2",...,"DEF10N_M"] 

    if len(code_list) == 0:
        return [[]]
    r = compute_power_set(code_list[:-1])
    return r + [s + [code_list[-1]] for s in r] # [["DEF101_1, DEF101_2,..."],["DEF101_1","DEF102_1",...],...[...]]
                                                # todas las combinaciones, luego filtraremos cuando se repite un ramo c:

def filter_set(power_set, n):
    filtered_set = []
    for permutation in power_set:
        code_plus_section_list = []
        code_list = []
        if len(permutation) == n:
            for element in permutation: 
                if element.split("_")[0] in code_list:
                    break
                code_plus_section_list.append(element)
                code_list.append(element.split("_")[0])
        if len(code_plus_section_list) == n:
            filtered_set.append(code_plus_section_list)
    return filtered_set