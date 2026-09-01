import pandas as pd
import numpy as np

# Create DataFrame with random values
np.random.seed(10)

df = pd.DataFrame(
    np.random.randint(-20, 21, size=(10, 4)),
    columns=["A", "B", "C", "D"]
)

print("Original DataFrame")
print(df)

# Function to highlight values
def highlight(value):
    if value < 0:
        return "color:red"
    else:
        return "color:black"

# Apply styling
styled = df.style.map(highlight)

# Save styled DataFrame as HTML
styled.to_html("highlight_numbers.html")

print("\nStyled DataFrame saved as 'highlight_numbers.html'")