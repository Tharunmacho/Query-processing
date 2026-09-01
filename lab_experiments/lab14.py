import pandas as pd
import numpy as np

# Create a sample DataFrame with some missing values
data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Age': [25, np.nan, 30, 22, np.nan],
    'Score': [85, 90, np.nan, np.nan, 95]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replace missing values
# For string column, fill with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')
# For numeric age column, fill with mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())
# For score column, fill with 0
df['Score'] = df['Score'].fillna(0)

print("\nDataFrame after replacing missing values:")
print(df)
