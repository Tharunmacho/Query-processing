import pandas as pd

# Read the CSV file
df = pd.read_csv("l9.csv")

# Display dataset
print("Sales Dataset")
print(df)

# Create Pivot Table
pivot = pd.pivot_table(
    df,
    values="SaleAmount",
    index=["Region", "Manager", "Salesman"],
    aggfunc="sum"
)

print("\nPivot Table")
print(pivot)