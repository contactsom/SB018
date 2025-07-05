import matplotlib.pyplot as plt
import numpy as np

'''
Combine Color Size and Alpha
You can combine a colormap with different sizes of the dots. This is best visualized if the dots are transparent:
'''

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()