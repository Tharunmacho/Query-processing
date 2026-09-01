import os
import matplotlib.pyplot as plt

# Write a temporary data file
data_content = """1 2
2 4
3 1
4 5
5 3
"""
data_filename = "lab23_data.txt"

with open(data_filename, "w", encoding="utf-8") as f:
    f.write(data_content)
print(f"Created data file '{data_filename}'")

# Read the values from the text file
x = []
y = []
with open(data_filename, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            x.append(float(parts[0]))
            y.append(float(parts[1]))

print(f"Read X: {x}")
print(f"Read Y: {y}")

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='s', color='green', linestyle='--', label='Data from File')

# Add labels and title
plt.xlabel('X Axis (from file)')
plt.ylabel('Y Axis (from file)')
plt.title('Line Plot from File Data')

# Add legend
plt.legend()

# Save the plot
output_image = 'lab23_file_line_plot.png'
plt.savefig(output_image)
plt.close()

print(f"Line plot saved to '{output_image}'")
