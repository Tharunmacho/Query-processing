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

print("\nDetecting missing values (isna):")
print(df.isna())
