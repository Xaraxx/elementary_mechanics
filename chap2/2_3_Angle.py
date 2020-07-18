import math

def angle_theta(x, y):
    theta = math.atan(y/x)
    print(theta)
    return theta

if __name__ == "__main__":
    x = 1
    y = 1
    angle_theta(x, y)