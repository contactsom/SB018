import matplotlib.pyplot as plt
import numpy as np

'''
You can plot as many lines as you like by simply adding more plt.plot() functions:
'''
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()