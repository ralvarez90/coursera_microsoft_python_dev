"""
_05_example_data_frame.py

Una manera de crear un DataFrame de pandas es a partir de un diccionario.
"""
import pandas as pd

# Sample data.
data = {
    'age': [25, 30, 35, 40],
    'gender': ['male', 'female', 'male', 'female'],
    'income': [50000, 60000, 75000, 55000],
}

# Create dataframe.
df = pd.DataFrame(data)

# Convert 'gender' to categorical variable.
df['gender'] = df['gender'].astype('category')

# Calculate average income.
average_income = df['income'].mean()
print(f'average income: {average_income}')
print('-' * 60 + '\n')

# Count the number of males and females
gender_counts = df['gender'].value_counts()
print(gender_counts)
print('-' * 60 + '\n')
print(gender_counts.to_dict())
