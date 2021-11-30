import math


def leibniz(tol, itmax):
"""
    Traccia 4 4.04.13
"""
    i = 0
    j = 3
    b = 0
    r = 1
    while i < itmax:

        if b == 0:
            r = r - (1 / j)
            b = 1
        else:
            r = r + (1 / j)
            b = 0

        if math.fabs(math.pi - (4*r)) < tol:
            return i

        j += 2
        i += 1

if __name__ == '__main__':
    print(leibniz(1e-2, 50))
