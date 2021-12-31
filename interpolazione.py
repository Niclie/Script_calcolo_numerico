import numpy as np
import matplotlib.pyplot as plt

def interpola(f, a, b, n):
    """Sfrutta la funzione lagrange per disegnare il grafico della funzione f con i relativi n punti equidistanti compresi fra a e b e il grafico del polinomio ottenuto dalla funzione lagrange

    Args:
               f (Funzione): funzione da interpolare
        [a, b] (Intervallo): intervallo di rappresentazione
                n (Integer): Numero di nodi equidistanti
    """
    
    x = np.linspace(a, b, n)
    y = f(x)
    xx = np.linspace(a, b, 100)
    pX = lagrange(x, y, xx)
    fX = f(xx)
    
    plt.plot(x, y, 'o', xx, fX, xx, pX, 'g')
    plt.legend('punti', 'f(x)')
    plt.title('Interpolazione polinomiale')
    plt.show()
    
    return

def lagrange(x, y, xx):
    """Funzione che effetua l'interpolazione di Lagrange

    Args:
         x (Array di float): Array dei nodi
         y (Array di float): Array di ordinate
        xx (Array di float): Array di ascisse

    Returns:
        [Array di float]: Array che contiene le valutazioni del polinomio che interpola i dato x e y nei punti dell'array xx
    """
    m = len(xx)
    n = len(x)
    yy = np.zeros((m, 1))
    
    for j in range(m):
        for k in range(n):
            lk = 1
            for i in range(n):
                if i != k:
                    lk *= (xx[j] - x[i])/(x[k] - x[i])
                else:
                    i += 1
            yy[j] = yy[j] + lk * y[k]
    
    return yy


def f(x):
    return (np.sin(x))

def g(x):
    return np.exp(-x)*(np.cos(x))

def h(x):
    return 1/(x**2 + 1)

def main():    
    #interpola(f, 0, np.pi, 5)    
    #interpola(g, 0, np.pi, 5)    
    interpola(h, -5, 5, 5)    

    
    return

if __name__ == "__main__":
    main()