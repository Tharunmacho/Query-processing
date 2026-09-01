import pandas as pd
import numpy as np

# Create DataFrame with random values
np.random.seed(12)
df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=["A", "B", "C", "D"]
)

print("Original DataFrame:")
print(df)

# Set background black and font color yellow
styled_df = df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow'
})

# Save to HTML
output_file = "lab12_black_yellow.html"
styled_df.to_html(output_file)

print(f"\nStyled DataFrame saved to '{output_file}'")
