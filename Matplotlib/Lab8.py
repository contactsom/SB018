import matplotlib.pyplot as plt
import numpy as np

'''
You can use the keyword argument marker to emphasize each point with a specified marker:
'''

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()