grid = {
    'labels': {
        'block_label': {
            'row': 0,
            'column': 0,
            'sticky': 'we',
            'padx': 1,
            'pady': 1
        }
    }
}

week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
block_list = ['block1', 'block2', 'block3', 'block4', 'block5', 'block6', 'block7']

for day_index in range(len(week_days)): # range 0 -> 5
    grid['labels'][week_days[day_index]] = {'row':0, 'column':day_index+1, 'sticky':'s', 'padx':1, 'pady':1}

for block_index in range(len(block_list)): # range 0 -> 6
    grid['labels'][block_list[block_index]] = {'row':block_index+1, 'column':0, 'sticky':'we', 'padx':1, 'pady':1}


