import matplotlib.pyplot as plt
import numpy as np

'''
Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):
'''
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()