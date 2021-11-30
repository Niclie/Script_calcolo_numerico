import numpy


def fattlu(m):
    """
    fattorizzazione LU di a

    Args:
        a (Matrice di reali): Matrice di cui calcolare la fattorizzazione LU
    """
    
    a = numpy.copy(m)
    
    n = a.shape[0]
    if n != a.shape[1]:
        raise Exception("Matrice non quadrata")
    
    l = numpy.identity(n)
    for k in range(n-1):
        for i in range(k+1, n):
            m = -(a[i][k]/a[k][k])
            for j in range(k+1, n):
                a[i][j] = a[i][j]+(m*a[k][j])
            l[i][k] = -m
    
    return l, numpy.triu(a)
    

def main():
    """a = numpy.array([[2,1,0,-1],
                     [-2,-2,1,-1],
                     [4,2,-1,-1],
                     [0,2,-3,2]])"""
                     
    a = numpy.random.randint(1, 9, (3, 3))
    
    print(a, "\n")
    
    [x, y] = fattlu(a)
    
    print(x,"\n")
    print(y)
    
    print(x.dot(y))
    
    return