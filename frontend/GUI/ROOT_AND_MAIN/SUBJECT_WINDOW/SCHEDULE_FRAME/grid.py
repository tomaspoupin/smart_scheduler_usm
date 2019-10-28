grid = {
    'labels': {
        'block_label': {
            'row': 0,
            'column': 0,
            'sticky': 'we',
            'padx': 1,
            'pady': 1
        }
    },
    "checkboxes":{}
}


week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
block_list = ['block1', 'block2', 'block3', 'block4', 'block5', 'block6', 'block7']

for day_index in range(len(week_days)): # range 0 -> 5
    grid['labels'][week_days[day_index]] = {'row':0, 'column':day_index+1, 'sticky':'we', 'padx':1, 'pady':1}

for block_index in range(len(block_list)): # range 0 -> 6
    grid['labels'][block_list[block_index]] = {'row':block_index+1, 'column':0, 'sticky':'we', 'padx':1, 'pady':1}

for day_index in range(len(week_days)):
    for block_index in range(len(block_list)):
        day_block_code = week_days[day_index]+'_'+block_list[block_index] # Ex: monday_block1
        grid["checkboxes"][day_block_code] = {'row':block_index+1, 'column':day_index+1, 'sticky': 'we', 'padx': 1, 'pady':1}


# week_days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
# block_list = ['1-2', '3-4', '5-6', '7-8', '9-10', '11-12', '13-14']
# block_list = []
# for i in range(1,8): #[1, 2, ... 6, 7]
#     block.append(str(2*i-1)+'-'+str(2*i)))
