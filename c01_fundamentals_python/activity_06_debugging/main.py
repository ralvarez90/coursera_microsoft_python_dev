from typing import Hashable, Any

import pandas as pd

# Load csv file
insectsDf = pd.read_csv('insect_collection.csv')

# Convert the DataFrame to a list of dictionaries
allInsectsData = insectsDf.to_dict('records')

# Get the first element
firstInsect: dict[Hashable, Any] | None = None
firstDigitOfLegs: int | None = None
if len(allInsectsData) > 0:
    firstInsect = allInsectsData[0]
    firstDigitOfLegs = insectsDf.get('legs')

if firstInsect is not None and firstDigitOfLegs is not None:
    print(f'The first digit of the number of legs the {firstInsect["name"]} has is: {firstDigitOfLegs}')
