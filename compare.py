import numpy as np
from sys import getsizeof
import random
from timeit import Timer

X = [random.randint(0, 200) for _ in range(10000)]
Y = [random.randint(0, 200) for _ in range(10000)]
# Convert to a Numpy Array
np_X = np.array(X, np.int64)
np_Y = np.array(Y, np.int64)


# 2 listen mit 2 werten zusammen addieren

def python():
    res = [X[i] + Y[i] for i in range(10000)]
    return res


def numpy():
    res = np_X + np_Y
    return res


time_python = Timer("python()", "from __main__ import python").timeit(10)
time_numpy = Timer("numpy()", "from __main__ import numpy").timeit(10)

print(f"Python list size: {getsizeof(X)}")
print(f"Numpy array size: {getsizeof(np_X)}")
print(f"Time in Python was: {time_python}")
print(f"Time in Numpy was: {time_numpy}")
print(f"Numpy was {time_python/time_numpy} times faster and {getsizeof(X)/getsizeof(np_X)} times less memory consuming")
