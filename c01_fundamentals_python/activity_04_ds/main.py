import pandas as pd
import pathlib

# read csv fila
file_name = 'inventory.csv'
if not pathlib.Path(file_name).exists():
    error_msg = f'File "{file_name}" don\'t exists.'
    raise FileNotFoundError(error_msg)

# get inventory dataframe
inventory_df = pd.read_csv(file_name)

# extract product names
inventory = inventory_df['product_name'].tolist()

# remove of list Cheesy Chompers
if 'Cheesy Chompers' in set(inventory):
    inventory.remove('Cheesy Chompers')

# show update inventory
print('\nUpdated Inventory:')
[print(f'- {item}') for item in inventory]

print('A new shipment of gourmet goodies has arrived!')

# new shipment of goodies! (provided as a string)
new_items_str = 'Squeaky Sausages, Tuna Tidbits, Chruncy Carrtos'
new_items = new_items_str.split(sep=', ')

# Update the inventory list by adding 'new items'
inventory.extend(new_items)
print('\nUpdated Inventory:')
[print(f'- {item}') for item in inventory]

# create some products IDs as tuples
product_id1 = ('Salmon Snacks', 'Small')
product_id2 = ('Cheesy Chompers', 'Medium')
product_id3 = ('Peanut Butter Biscuits', 'Large')
print("Product IDs:")
print(product_id1)
print(product_id2)
print(product_id3)
print('\n' + '-'*60 + '\n')

# Load againg inventoru data from csv
inventory_df = pd.read_csv(file_name)

# set the 'product_name' column as the index
inventory_df.set_index(keys='product_name', inplace=True)

# convert the dataframe directly to a dictionary
inventory_dict = inventory_df['stock_level'].to_dict()
print(inventory_dict)

# Add "Puppy Snacks" to the inventoru
inventory_dict["Puppy Snacks"] = 40

# Update "Chessy Chompers" in the inventory and assign it the value of 20
inventory_dict['Cheesy Chompers'] = 20
print(inventory_dict)

# Remove 'Peanut Butter Biscuits'
if 'Peanut Butter Biscuits' in set(inventory_dict.keys()):
    del inventory_dict['Peanut Butter Biscuits']

# Show uptadetd invenroty
print(f'\nUpdated Inventory:')
[print(f'- ({k}, {v})') for k, v in inventory_dict.items()]