import numpy as np

data = np.genfromtxt('DATASet.csv', delimiter=",", skip_header=1)
print(data)
print(type(data))

