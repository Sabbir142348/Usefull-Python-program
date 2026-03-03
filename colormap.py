import matplotlib.pyplot as plt
import numpy as np

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

colormaps = ['viridis', 'plasma', 'coolwarm', 'jet']

fig, axs = plt.subplots(len(colormaps), figsize=(6, 2 * len(colormaps)))

for i, cmap in enumerate(colormaps):
    axs[i].imshow(gradient, aspect='auto', cmap=cmap)
    axs[i].set_title(cmap)
    axs[i].axis('off')

plt.tight_layout()
plt.show()