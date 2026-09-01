import pandas as pd

# Create a sample DataFrame with string codes
df = pd.DataFrame({
    'name_code': ['c0001', '1000c', 'b00c2', 'b2c02', 'c2222']
})

print("Original DataFrame:")
print(df)

# Find the index of the substring 'c' in the column 'name_code'
# str.find() returns the index of the character in the string (-1 if not found)
df['index_of_c'] = df['name_code'].str.find('c')

print("\nDataFrame with character index of 'c':")
print(df)
