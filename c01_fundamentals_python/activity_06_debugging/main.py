from typing import Hashable, Any

import pandas as pd

# Load csv file
insects_df = pd.read_csv('insect_collection.csv')

# Convert the DataFrame to a list of dictionaries
all_insects_data = insects_df.to_dict('records')

# Get the first element
first_insect: dict[Hashable, Any] | None = None
first_digit_of_legs: int | None = None
if len(all_insects_data) > 0:
    first_insect = all_insects_data[0]
    first_digit_of_legs = insects_df.get('legs')

if first_insect is not None and first_digit_of_legs is not None:
    print(f'The first digit of the number of legs the {first_insect["name"]} has is: {first_digit_of_legs}')
