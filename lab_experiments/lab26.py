import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure for multiple plots
plt.figure(figsize=(10, 8))

# Subplot 1 (Top)
plt.subplot(2, 1, 1)
plt.plot(x, y1, color='purple', label='Sine Wave')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()

# Subplot 2 (Bottom)
plt.subplot(2, 1, 2)
plt.plot(x, y2, color='orange', label='Cosine Wave')
plt.title('Cosine Wave')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.grid(True)
plt.legend()

# Adjust layout to prevent overlap
plt.tight_layout()

# Save plot
output_image = 'lab26_multiple_plots.png'
plt.savefig(output_image)
plt.close()

print(f"Multiple plots layout saved to '{output_image}'")
