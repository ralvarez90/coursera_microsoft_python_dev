import os

import pandas as pd

# file name in the folder
file_name = 'grocery_list.csv'

# load file data if exists
if os.path.exists(path=file_name):

    # load the grocery list from the cvs file
    grocery_list_df = pd.read_csv(file_name)

    # use item head in a csv file
    grocery_list = grocery_list_df['item'].tolist()

    # add kiwis and raspberries to the list
    items_to_add = ['Kiwis', 'Raspberries']
    for item in items_to_add:
        grocery_list.append(item)

    # get user input
    new_item = input('Enter an item to add to you grocery list: ')
    new_item = new_item.strip().title()

    # add if new item dont exists
    if new_item not in grocery_list:
        grocery_list.append(new_item)
        print('Updated list:')
        for item in grocery_list:
            print(f'- {item}')
    else:
        print(f'Item "{new_item}" already exists in grocery list.')

    # append some items in list
    grocery_list.append('Cinnamon')
    grocery_list.append('Paprika')

    # remove some items in list
    if 'Eggs' in grocery_list:
        grocery_list.remove('Eggs')
    if 'Apples' in grocery_list:
        grocery_list.remove('Apples')

    # Show update list
    print('\nYour Update Grocery List (after removing items)')
    for item in grocery_list:
        print(f'- {item}')

else:
    error_msg = f'File "{file_name}" was not found in current directory.'
    print(error_msg)
