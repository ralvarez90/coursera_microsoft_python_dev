"""
_18_transform_data.py
"""
from pprint import pprint

import numpy as np
import pandas as pd

from utils import StringFormatter, UtilConsole

SALES_DATA_PATH: str = './datacsv/sales_data.csv'

# Load data frame from file of sales
salesDF = pd.read_csv(SALES_DATA_PATH)

# Show the head DataFrame
pprint(StringFormatter.make_title('salesDF.head()'))
pprint(salesDF.head())

# Sort info by sales
print(StringFormatter.make_title('salesDF.sort_values(by="Sales", ascending=False)'))
sortedSalesDF = salesDF.sort_values(by='Sales', ascending=False)
pprint(sortedSalesDF.head())

# Grouping by Region and calculate total sales of each region
print(StringFormatter.make_title('salesDF.groupby("Region")["Sales"].sum()'))
salesByRegion = salesDF.groupby('Region')['Sales'].sum().sort_values(ascending=False)
pprint(salesByRegion)

# Filtering
print(StringFormatter.make_title('salesDF["Sales"].mean()'))
meanSales: float = salesDF['Sales'].mean()
pprint(meanSales)

# Filtering with a boolean mask
print(StringFormatter.make_title('salesDF[salesDF["Sales"] > 1300]'))
filteredSales = salesDF[salesDF['Sales'] > 1300]
pprint(filteredSales)


def calculateDiscount(sales: float) -> float:
    return sales * 0.9


# Using an apply method
print(StringFormatter.make_title('salesDF["Sales"].apply(calculateDiscount)'))
salesDF['Discount_Sales'] = salesDF['Sales'].apply(calculateDiscount)
pprint(salesDF.head())

# Using pivot_table
print(StringFormatter.make_title('df.pivot_table(index="Year", columns="Language", values="Proyectos")'))
df = pd.DataFrame({
    'Year': [2024, 2024, 2025, 2025, 2025],
    'Language': ['Python', 'Swift', 'Python', 'Swift', 'Dart'],
    'Proyectos': [3, 2, 5, 4, 2],
    'Horas': [30, 40, 50, 60, 20],
})
pprint(df.pivot_table(index='Year', columns='Language', values='Proyectos'))
print()
pprint(salesDF.pivot_table(index='Region', columns='Product', values='Sales'))

# Sample dataframe with missing values
print(StringFormatter.make_title('dfWithMissingValues'))
dfWithMissingValues = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})
pprint(dfWithMissingValues)
dfFilled = dfWithMissingValues.fillna(0)
dfDropped = dfWithMissingValues.dropna()
pprint(dfFilled)
pprint(dfDropped)

# Concat example
print(StringFormatter.make_title('pd.concat( [df1, df2])'))
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
dfConcat = pd.concat([df1, df2])
print(dfConcat)

# End application
UtilConsole.system_pause()
