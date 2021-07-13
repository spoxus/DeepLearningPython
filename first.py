print('hi')

def dummy():
    print('hihihi')
    return 1

a = dummy()
print(a)

import numpy as np

def mean_squared_error(y, t):
    return np.sum((y - t) ** 2) / 2.0

y = 0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0
y = np.array(y)

t = 0, 0, 1, 0, 0, 0, 0, 0, 0, 0
t = np.array(t)

mse = mean_squared_error(y, t)
print(mse)

y1 = 0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0
y1 = np.array(y1)
mse = mean_squared_error(y1, t)
print(mse)

def cross_entropy_error(y, t):
    delta = 1e-8
    return -np.sum(t * np.log(y + delta))

cer = cross_entropy_error(y, t)
print(cer)

cer = cross_entropy_error(y1, t)
print(cer)