import matplotlib.pyplot as plt
import numpy as np

'''
Compare Plots
In the example above, there seems to be a relationship between speed and age, 
but what if we plot the observations from another day as well? Will the scatter plot tell us something else?
'''

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()