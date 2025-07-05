import matplotlib.pyplot as plt
import numpy as np

'''
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
'''
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()