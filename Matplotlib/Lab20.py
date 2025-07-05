import matplotlib.pyplot as plt
import numpy as np

'''
You can use the keyword argument linewidth or the shorter lw to change the width of the line.
'''
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()