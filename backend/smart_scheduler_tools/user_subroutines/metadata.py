def create_metadata(schedule=None, code=None, section=None):
    metadata = {
        'Mon': ['','','','','','',''],
        'Tue': ['','','','','','',''],
        'Wen': ['','','','','','',''],
        'Thu': ['','','','','','',''],
        'Fri': ['','','','','','',''],
        'Sat': ['','','','','','','']
        }
    if schedule is None or code is None or section is None:
        return metadata

    schedule_dict = schedule.get_dict()
    for day in schedule_dict:
        for block_index in range(len(schedule_dict[day])):
            if schedule_dict[day][block_index] == 1:
                metadata[day][block_index] = code + '_' + str(section)
    return metadata

def add_metadatas(metadata_one, metadata_two):
    result_metadata = {
        'Mon': ['','','','','','',''],
        'Tue': ['','','','','','',''],
        'Wen': ['','','','','','',''],
        'Thu': ['','','','','','',''],
        'Fri': ['','','','','','',''],
        'Sat': ['','','','','','','']
        }
    for day in result_metadata:
        for block_index in range(len(result_metadata[day])):
            if metadata_one[day][block_index] and metadata_two[day][block_index]:
                result_metadata[day][block_index] = \
                    metadata_one[day][block_index] + ' ' + metadata_two[day][block_index]
            elif metadata_one[day][block_index]:
                result_metadata[day][block_index] = metadata_one[day][block_index]
            elif metadata_two[day][block_index]:
                result_metadata[day][block_index] = metadata_two[day][block_index]                       
    return result_metadata