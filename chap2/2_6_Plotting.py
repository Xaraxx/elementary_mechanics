import matplotlib.pyplot as plt
import numpy as np

def one_over_x(x, n):
    f = 1/(x**n)
    print(f)
    return f

if __name__ == "__main__":
    x1 = np.arange(-1.0, 1.1, 0.2)
    n = [1, 2, 3]
    vec_one_over_x = np.vectorize(one_over_x)
    plt.plot(x1, vec_one_over_x(x1, n[0]), 'r--', x1, vec_one_over_x(x1, n[1]), 'b.-', x1, vec_one_over_x(x1, n[2]), 'g.-')
    plt.show()



