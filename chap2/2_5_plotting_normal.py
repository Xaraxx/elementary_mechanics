import matplotlib.pyplot as plt
import numpy as np
import math

def normal_dist(x, mu, sigma):
    P = (1/(math.sqrt(2*math.pi*sigma**2)))*math.exp(-(x - mu)**2/(2 * sigma**2))
    print(P)
    return P


if __name__ == "__main__":
    x1 = np.arange(-5.0, 5.1, 0.1)
    mu = 0
    sigma = 1
    vec_normal_dist = np.vectorize(normal_dist)
    plt.plot(x1, vec_normal_dist(x1, mu, sigma), 'bo')
    plt.show()

    sigma1 = 2
    sigma2 = 0.5

    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    ax1.plot(x1, vec_normal_dist(x1, mu, sigma1), 'ko-')
    ax1.set(title='Normal distribution for two sigma values', ylabel='sigma = 2')

    ax2.plot(x1, vec_normal_dist(x1, mu, sigma2), 'r.-')
    ax2.set(ylabel='sigma = 2')

    plt.show()

    # Is this the part d to the exercise
    mu1 = 1
    mu2 = 2

    plt.plot(x1, vec_normal_dist(x1, mu, sigma1), 'r--', x1, vec_normal_dist(x1, mu1, sigma), 'b.-', x1, vec_normal_dist(x1, mu2, sigma), 'g.-')
    plt.show()
    
