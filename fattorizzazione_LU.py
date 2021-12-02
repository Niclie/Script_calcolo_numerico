from numpy import *


def triang_sup(a, b, tol=1e-15):
    """
    Algoritmo di sostituzione all'indietro per sistemi lineari triangolari superiori

    Args:
        a (matrice di float): matrice dei coefficienti
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


def fattlu(m):
    """
    Fattorizza m in forma LU

    Args:
        m (matrice di float): matrice da fattorizzare in LU

    Raises:
        Exception: eccezione generica in caso di matrice non quadrata

    Returns:
        matrice L: matrice triangolare inferiore speciale L
        matrice U: matrice triangolare superiore U
    """
    
    a = copy(m)
    
    n = a.shape[0]
    if n != a.shape[1]:
        raise Exception("Matrice non quadrata")
    
    l = identity(n)
    for k in range(n-1):
        for i in range(k+1, n):
            m = -(a[i][k]/a[k][k])
            for j in range(k+1, n):
                a[i][j] = a[i][j]+(m*a[k][j])
            l[i][k] = -m
    
    return l, triu(a)


def gauss_max_pivot_par(a_, b_, tol=1e-15):
    n = a_.shape[0]
    if n != a_.shape[1]:
        raise Exception("Matrice non quadrata")
    
    a = copy(a_)
    b = copy(b_)
        
    for k in range(n-1):
        s = k
        piv = abs(a[k][k])
        for i in range(k+1, n):
            if abs(a[i][k]) > piv:
                s = i
                piv = abs(a[i][k])
        if s != k:
            a[[k, s]] = a[[s, k]]
            b[[k, s]] = b[[s, k]]
            
        for i in range(k+1, n):
            m = -(a[i][k]/a[k][k])
            for j in range(k+1, n):
                a[i][j] = a[i][j]+(m*a[k][j])
            
            b[i] = b[i]+(m*b[k])
                    
    
    return triu(a), b


def main():
    a = array([[1, -2, 3], [-1, 2, 1], [2, -1, -1]], float)
    b = array([1, 0, -1], float)
    
    #a = array([[1, -2, 0, 1], [-1, 1, 2, 0], [2, -3, 0, 2], [-1, 2, 0, 2]], float)
    #b = array([-1, 0, 1, 2], float)
    
    [x, y] = gauss_max_pivot_par(a, b)
    print(x, "\n")
    print(y, "\n")
    
    print(triang_sup(x, y))    
    
    return


if __name__ == "__main__":
    main()