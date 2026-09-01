import matplotlib.pyplot as plt

# Data
x = [10, 20, 30, 40, 50]
y1 = [20, 40, 10, 30, 50]
y2 = [40, 10, 30, 20, 10]
y3 = [10, 30, 50, 40, 20]

# Create plot
plt.figure(figsize=(8, 5))

# Plot lines with custom width and color
plt.plot(x, y1, label='Line 1 (width=3, red)', color='red', linewidth=3)
plt.plot(x, y2, label='Line 2 (width=5, blue)', color='blue', linewidth=5)
plt.plot(x, y3, label='Line 3 (width=1, green)', color='green', linewidth=1)

# Add title, labels, grid, and legend
plt.title('Multiple Lines with Different Widths & Colors')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.legend()

# Save plot
output_image = 'lab25_multi_lines_plot.png'
plt.savefig(output_image)
plt.close()

print(f"Multi-line plot saved to '{output_image}'")
