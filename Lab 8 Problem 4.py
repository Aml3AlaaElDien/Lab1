import math
def recpol(x, y):

    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    theta = theta % (2 * math.pi)

    return r, theta