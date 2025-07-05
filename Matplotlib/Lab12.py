import matplotlib.pyplot as plt
import numpy as np

'''
You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
'''

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()