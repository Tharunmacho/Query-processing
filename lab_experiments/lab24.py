import os
import pandas as pd
import matplotlib.pyplot as plt

# Financial data content
csv_content = """Date,Open,High,Low,Close
10-03-16,774.25,776.065002,769.5,772.559998
10-04-16,776.030029,778.710022,772.890015,776.429993
10-05-16,779.309998,782.070007,775.650024,776.469971
10-06-16,779,780.47998,775.539978,776.859985
10-07-16,779.659973,779.659973,770.75,775.080017
"""
csv_filename = "fdata.csv"

# Write the data file
with open(csv_filename, "w", encoding="utf-8") as f:
    f.write(csv_content)
print(f"Created financial data file '{csv_filename}'")

# Load financial data
df = pd.read_csv(csv_filename, sep=',', parse_dates=True, index_col=0)

print("\nFinancial DataFrame (Alphabet Inc.):")
print(df)

# Plot lines
df.plot(marker='o')

# Customize layout
plt.title('Alphabet Inc. Stock Prices (Oct 2016)')
plt.ylabel('Price')
plt.xlabel('Date')
plt.grid(True)

# Save plot
output_image = 'lab24_finance_plot.png'
plt.savefig(output_image)
plt.close()

print(f"\nFinancial line chart saved to '{output_image}'")
