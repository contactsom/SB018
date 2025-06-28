import numpy as np

data_struct = np.genfromtxt(
    'DATASet.csv',
    delimiter=",",
    names=True,         # Read header as field names
    dtype=None,         # Infer column types
    encoding=None       # Handle string types properly
)
print(data_struct.dtype.names)  # Tuple of column names
print(type(data_struct))        # → <class 'numpy.ndarray'>


