import numpy as np
import scipy.linalg as linalg


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
    (r, c) = np.shape(a)
    if r != np.size(b):
        raise Exception("Numero di equazini diverso dal numero di termini noti")

    x = np.zeros(r)

    for i in range(r-1, -1, -1):
        if abs(a[i][i]) < tol:
            print("determinante prossimo a zero")
            return np.NaN

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
    (r, c) = np.shape(a)
    if r != np.size(b):
        raise Exception("Numero di equazini diverso dal numero di termini noti")
    
    x = np.zeros(r)
    
    for i in range(0, r):
        if abs(a[i][i]) < tol:
            print("determinante prossimo a zero")
            return np.NaN

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
    
    n = m.shape[0]
    if n != m.shape[1]:
        raise Exception("Matrice non quadrata")
    
    a = np.copy(m)
    l = np.identity(n)
    for k in range(n-1):
        for i in range(k+1, n):
            m = -(a[i][k]/a[k][k])
            for j in range(k+1, n):
                a[i][j] = a[i][j]+(m*a[k][j])
            l[i][k] = -m
    
    return l, np.triu(a)


def gauss_max_pivot_par(a_, b_):
    """trasforma il sistema lineare dalla forma Ax = b alla forma Ux = b
    (vedi fattorizzazione LU) con l'algoritmo di elimizazione di gauss sfruttando il max pivot per rendere l'algoritmo più stabile

    Args:
        a_ (matrice di float): matrice dei coefficienti
        b_ (vettore di float): vettore dei termini noti

    Raises:
        Exception: eccezione generica in caso di matrice non quadrata

    Returns:
        matrice di float: matrice triangolare superiore
        vettore di float: nuovo vettore dei termini noti 
    """
    
    n = a_.shape[0]
    if n != a_.shape[1]:
        raise Exception("Matrice non quadrata")
    
    a = np.copy(a_)
    b = np.copy(b_)
        
    for k in range(n-1):
        max_row_index = np.argmax(abs(a[k:n, k])) + k
        a[[k, max_row_index]] = a[[max_row_index, k]]
        b[[k, max_row_index]] = b[[max_row_index, k]]
            
        for i in range(k+1, n):
            m = -(a[i][k]/a[k][k])
            for j in range(k+1, n):
                a[i][j] += (m*a[k][j])
            
            b[i] += (m*b[k])
                    
    
    return np.triu(a), b


def fattlu_pivot(m):
    """fattorizza m sfruttando la fattorizzazione LU con tecnica di pivot

    Args:
        m (matrice di float): matrice da fattorizzare

    Returns:
        matrice di 0 e 1: matrice di permutazione
        matrice di float: matrice triangolare inferiore speciale L
        matrice di float: matrice triangolare superiore U
    """
    
    n = m.shape[0]
    p = np.arange(0, n)
    a = np.copy(m)
    for k in range(n-1):
        max_row_index = np.argmax(abs(a[k:n, k])) + k
        p[[k, max_row_index]] = p[[max_row_index, k]]
        a[[k, max_row_index]] = a[[max_row_index, k]]
        
        for i in range(k+1, n):
            a[i][k] /= a[k][k]
            for j in range(k+1, n):
                a[i][j] -= a[i][k]*a[k][j]            
    
    l = np.tril(a, -1)
    np.fill_diagonal(l, 1)
    return p, l, np.triu(a)


def matrice_inversa_lu(m):
    """Funzione che permette il calcolo dell'inversa attraverso la fattorizzazione LU

    Args:
        m (matrice di float): matrice di cui calcolare l'inversa

    Raises:
        Exception: eccezione generica in caso di matrice non quadrata

    Returns:
        z: matrice inversa di m
    """
    n = m.shape[0]
    if n != m.shape[1]:
        raise Exception("Matrice non quadrata")
    
    a = np.copy(m)
    id = np.identity(n)
    for k in range(n-1):
        max_row_index = np.argmax(abs(a[k:n, k])) + k
        a[[k, max_row_index]] = a[[max_row_index, k]]
        id[[k, max_row_index]] = id[[max_row_index, k]]
            
        for i in range(k+1, n):
            m = -(a[i][k]/a[k][k])
            for j in range(k+1, n):
                a[i][j] += (m*a[k][j])
            
            for j in range(0, n):
                id[i][j] += (m*id[k][j])
    
    z = np.zeros((n, n))
    for i in range(n):
        z[:, i] = triang_sup(a, id[:, i])
    
    return z

def main():
    #a = np.array([[1, -1, 0], [2, 1, -1], [0, -2, 1]], float)
    a = np.array([[0, -1, 2], [1, 0, -1], [0, 1, 0]])
    print(a, "\n================================")
    x = matrice_inversa_lu(a)
    print(x, "\n")
    print(a.dot(x))
    
    return


if __name__ == "__main__":
    main()