import os

import pandas as pd

# file name in the folder
fileName = 'grocery_list.csv'

# load file data if exists
if os.path.exists(path=fileName):

    # load the grocery list from the cvs file
    groceryListDf = pd.read_csv(fileName)

    # use item head in a csv file
    groceryList = groceryListDf['item'].tolist()

    # add kiwis and raspberries to the list
    itemsToAdd = ['Kiwis', 'Raspberries']
    for item in itemsToAdd:
        groceryList.append(item)

    # get user input
    newItem = input('Enter an item to add to you grocery list: ')
    newItem = newItem.strip().title()

    # add if new item don't exists
    if newItem not in groceryList:
        groceryList.append(newItem)
        print('Updated list:')
        for item in groceryList:
            print(f'- {item}')
    else:
        print(f'Item "{newItem}" already exists in grocery list.')

    # append some items in list
    groceryList.append('Cinnamon')
    groceryList.append('Paprika')

    # remove some items in list
    if 'Eggs' in groceryList:
        groceryList.remove('Eggs')
    if 'Apples' in groceryList:
        groceryList.remove('Apples')

    # Show update list
    print('\nYour Update Grocery List (after removing items)')
    for item in groceryList:
        print(f'- {item}')

else:
    errMsg = f'File "{fileName}" was not found in current directory.'
    print(errMsg)
