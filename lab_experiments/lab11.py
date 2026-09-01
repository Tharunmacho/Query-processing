import pandas as pd
import numpy as np

# Create DataFrame with random values
np.random.seed(11)
df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=["A", "B", "C", "D"]
)

# Convert some values to NaN
df.iloc[1, 2] = np.nan
df.iloc[3, 0] = np.nan
df.iloc[5, 3] = np.nan
df.iloc[8, 1] = np.nan

print("Original DataFrame with NaNs:")
print(df)

# Highlight NaN values (background color yellow)
def highlight_nan(val):
    if pd.isna(val):
        return 'background-color: yellow'
    return ''

# Apply style
styled_df = df.style.map(highlight_nan)

# Save to HTML
output_file = "lab11_highlight_nan.html"
styled_df.to_html(output_file)

print(f"\nStyled DataFrame saved to '{output_file}'")
