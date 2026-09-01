import matplotlib.pyplot as plt

# X and Y coordinates
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', color='blue', linestyle='-', label='Sample Trend')

# Add labels and title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Sample Line Plot')

# Add legend
plt.legend()

# Save the plot
output_image = 'lab22_line_plot.png'
plt.savefig(output_image)
plt.close()

print(f"Line plot drawn and saved to '{output_image}'")
