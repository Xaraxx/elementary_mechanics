# In this file you may find some code samples of how to use matplotlib
# this library has an excelent documentation, is esay to read and understand.

import matplotlib.pyplot as plt
import matplotlib
import tkinter
matplotlib.use('TkAgg')


plt.plot([1,2,3,4,5])
plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.show()

# another boring line

x = [1,2,3,4,5]
y = [6,17,8,9,10]

plt.plot(x, y, 'ro')
plt.axis([0, 6, 0, 15])
plt.show()


import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)
        }

data['b'] = data['a'] + 10 * np.random.randn(50) 
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()