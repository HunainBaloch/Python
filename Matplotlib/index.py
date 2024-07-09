import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axes
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Plot on the first subplot
ax[0].plot(x, y1, 'r-', label='Sine Wave')
ax[0].set_title('Sine Wave')
ax[0].set_xlabel('x')
ax[0].set_ylabel('sin(x)')
ax[0].legend()
ax[0].grid(True)

# Plot on the second subplot
ax[1].plot(x, y2, 'b-', label='Cosine Wave')
ax[1].set_title('Cosine Wave')
ax[1].set_xlabel('x')
ax[1].set_ylabel('cos(x)')
ax[1].legend()
ax[1].grid(True)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
