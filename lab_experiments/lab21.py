import pandas as pd

# Create a sample DataFrame with mixed-case strings
df = pd.DataFrame({
    'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'David Parkes']
})

print("Original DataFrame:")
print(df)

# Swap cases of the 'Name' column
df['Name_Swapped'] = df['Name'].str.swapcase()

print("\nDataFrame after swapping cases of the 'Name' column:")
print(df)
