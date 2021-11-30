from numpy import *


def triang_sup(a, b, tol=1e-15):
    """
    Algoritmo di sostituzione all'indietro per sistemi lineari triangolari superiori

    Args:
        a (Matrice di float): matrice dei coefficienti
        b (vettore di float): vettore dei termini noti
        tol (float): tolleranza massima per i valori lungo la diagonale. Defaults to 1e-15.

    Raises:
        Exception: eccezione generica in caso di valore lungo la diagonale inferiore a tol

    Returns:
        vettore di float: vettore contenente i valori delle incognite x
    """
    (r, c) = shape(a)
    if r != size(b):
        raise Exception("Numero di equazini diverso dal numero di termini noti")

    x = zeros((r, 1))

    for i in range(r-1, -1, -1):
        if abs(a[i][i]) < tol:
            print("determinante prossimo a zero")
            return NaN

        sum = 0
        for j in range(i+1, r):
            sum = sum + (a[i][j] * x[j]) 
        
        x[i] = (b[i] - sum) / a[i][i]

    return x

def triang_inf(a, b, tol=1e-15):
    """
    Algoritmo di sostituzione in avanti per sistemi lineari triangolari inferiori


    Args:
        a (Matrice di float): matrice dei coefficienti
        b (vettore di float): vettore dei termini noti
        tol (float): tolleranza massima per i valori lungo la diagonale. Defaults to 1e-15.
    
    Raises:
        Exception: eccezione generica in caso di valore lungo la diagonale inferiore a tol

    Returns:
        vettore di float: vettore contenente i valori delle incognite x
    """
    (r, c) = shape(a)
    if r != size(b):
        raise Exception("Numero di equazini diverso dal numero di termini noti")
    
    x = zeros((r, 1))
    
    for i in range(0, r):
        if abs(a[i][i]) < tol:
            print("determinante prossimo a zero")
            return NaN

        sum = 0
        for j in range(0, i):
            sum = sum + (a[i][j] * x[j]) 
        
        x[i] = (b[i] - sum) / a[i][i]

    return x