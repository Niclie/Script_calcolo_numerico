import numpy as np

"""
Scrivere una funcion norma(a, s) con:
a: matrice generica
s: 1, inf

che restituisce la norma 1 o infinito della matrice a
"""

def norma(a, s):
    r, c = a.shape
    
    m = np.copy(a)
    if s == "1":
        m = np.transpose(m)
        r, c = c, r
    
    max = 0
    for i in range(r):
        sum = 0
        for j in range(c):
            sum += np.abs(m[i][j])
        if sum > max:
            max = sum
    
    return max