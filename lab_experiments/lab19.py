import os
import pandas as pd

# CSV content for mock world alcohol consumption dataset
csv_content = """Year,WHO region,Country,Beverage Types,Display Value
1986,Western Pacific,Viet Nam,Wine,0.00
1986,Americas,Uruguay,Other,0.50
1985,Africa,Cte d'Ivoire,Wine,1.62
1986,Americas,Colombia,Beer,4.27
1987,Americas,Saint Kitts and Nevis,Beer,1.98
1987,Americas,Guatemala,Other,0.00
1987,Africa,Mauritius,Wine,0.11
1985,Africa,Angola,Spirits,1.16
1986,Americas,Antigua and Barbuda,Spirits,2.23
1984,Africa,Nigeria,Other,6.10
"""

csv_filename = "world_alcohol.csv"

# Write the CSV file
with open(csv_filename, "w", encoding="utf-8") as f:
    f.write(csv_content)
print(f"Created mock dataset '{csv_filename}'")

# Read the dataset
df = pd.read_csv(csv_filename)

print("\nWorld Alcohol Consumption Dataset (first few rows):")
print(df.head())

# Dimensions or shape of the dataset
print("\nDimensions (shape) of the dataset:")
print(df.shape)

# Column names
print("\nColumn names of the dataset:")
print(df.columns.tolist())
