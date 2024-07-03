
import pandas as pd

ROOT = 'C:/Python Bootcamp/'

df = pd.read_csv(ROOT + 'df_estados_bank.csv')

# print(df.head())

missing_values = df.isnull().sum()

duplicates = df.duplicated().sum()

print('Nulos ', missing_values)
print('Duplicados ', duplicates)