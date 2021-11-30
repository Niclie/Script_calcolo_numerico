def frazioni_continue(x):
"""
    Traccia 3 20.11.14
"""
    i = len(x) - 2
    r = 1 / x[i+1]
    while i >= 0:
        r = x[i] + 1/r
        i = i - 1

    return r

if __name__ == '__main__':
    print(frazioni_continue([3, 4, 12, 4]))