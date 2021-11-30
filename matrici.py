import numpy

#Esempi di come una matrice può essere creata con numpy
def definisciMatrice():
    #a = numpy.array([[1, 2, 3],[4, 5, 6]])
    a = numpy.random.randint(0, 9, (3, 3))

    #Altri metodi:

    #Matrici di 0
    zero_matrix = numpy.zeros((3, 2))

    #Con arrange e shape
    #con shape() siamo in grado di leggere le dimensioni
    arrange_matrix = numpy.arange(6).reshape(2, 3)
    
    return a


    
#Seguono esempi di operazioni fra matrici:

def sum(a, b):
    return a + b

def mul(a, b):
    #* è usato per gli array
    return a.dot(b)

def trasposta(a):
    return a.transpose()


def main():
    a = definisciMatrice()
    b = definisciMatrice()

    print(a, "\n")
    print(b, "\n")

    print("trasposta di a =\n", trasposta(a), "\n")
    print("trasposta di b =\n", trasposta(b), "\n")
    print("a + b =\n", sum(a, b), "\n")
    print("a * b =\n", mul(a, b), "\n")

    print(a[1:2:, 1])

    
    return
