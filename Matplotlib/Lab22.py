import matplotlib.pyplot as plt
import numpy as np

'''
You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.
(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)
The x- and y- values come in pairs:
'''

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()