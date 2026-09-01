import pandas as pd
import numpy as np

# Create a sample DataFrame with varying number of NaNs per row
data = {
    'A': [1, np.nan, np.nan, 4, np.nan],
    'B': [np.nan, np.nan, np.nan, 5, 6],
    'C': [7, 8, np.nan, np.nan, np.nan],
    'D': [10, 11, 12, np.nan, np.nan]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Keep rows with at least 2 NaN values
filtered_df = df[df.isna().sum(axis=1) >= 2]

print("\nDataFrame keeping only rows with at least 2 NaN values:")
print(filtered_df)
