import pandas as pd
import pathlib

# read csv fila
fileName = 'inventory.csv'
if not pathlib.Path(fileName).exists():
    errMsg = f'File "{fileName}" don\'t exists.'
    raise FileNotFoundError(errMsg)

# get inventory dataframe
inventoryDf = pd.read_csv(fileName)

# extract product names
inventory = inventoryDf['product_name'].tolist()

# remove of list Cheesy Chompers
if 'Cheesy Chompers' in set(inventory):
    inventory.remove('Cheesy Chompers')

# show update inventory
print('\nUpdated Inventory:')
for item in inventory:
    print(f'- {item}')

print('A new shipment of gourmet goodies has arrived!')

# new shipment of goodies! (provided as a string)
newItemsStr = 'Squeaky Sausages, Tuna Tidbits, Chruncy Carrtos'
newItems = newItemsStr.split(sep=', ')

# Update the inventory list by adding 'new items'
inventory.extend(newItems)
print('\nUpdated Inventory:')
for item in inventory:
    print(f'- {item}')

# create some products IDs as tuples
productId1 = ('Salmon Snacks', 'Small')
productId2 = ('Cheesy Chompers', 'Medium')
productId3 = ('Peanut Butter Biscuits', 'Large')

print("Product IDs:")
print(productId1)
print(productId2)
print(productId3)
print('\n' + '-' * 60 + '\n')

# Load again inventory data from csv
inventoryDf = pd.read_csv(fileName)

# set the 'product_name' column as the index
inventoryDf.set_index(keys='product_name', inplace=True)

# convert the dataframe directly to a dictionary
inventoryDict = inventoryDf['stock_level'].to_dict()
print(inventoryDict)

# Add "Puppy Snacks" to the inventoru
inventoryDict["Puppy Snacks"] = 40

# Update "Chessy Chompers" in the inventory and assign it the value of 20
inventoryDict['Cheesy Chompers'] = 20
print(inventoryDict)

# Remove 'Peanut Butter Biscuits'
if 'Peanut Butter Biscuits' in set(inventoryDict.keys()):
    del inventoryDict['Peanut Butter Biscuits']

# Show updated inventory
print(f'\nUpdated Inventory:')
for k, v in inventoryDict.items():
    print(f'- {k}, {v}')
