from numpy import *

def bisezioni(f, a, b, tol=1e-8, it_max=50):
    """
    METODO DELLE SUCCESSIVE BISEZIONI

    Parameters
    ----------
    f: funzione di cui ricercare uno zero

    a,b: estremi dell'intervallo di lavoro

    tol: precisione richiesta

    it_max: numero massimo di iterate consentite

    Returns
    -------
    c: approssimazione di uno zero di f

    it: numero di iterate effettuate
    """

    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        print('la funzione non cambia di segno')
        return

    it = 0
    arresto = False
    while not arresto and it <= it_max:
        it = it + 1

        c = (a + b) / 2
        fc = f(c)
        if fc == 0:
            return c, it

        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc

        arresto = b - a < tol

    if not arresto:
        print("Precisione non raggiunta")

    return c, it


def direzione_costante(f, m, a, b, tol=1e-8, it_max=50):
    """
    METODO DELLE SUCCESSIVE BISEZIONI

    Parameters
    ----------
    f: funzione di cui ricercare uno zero

    m: costante

    a,b: estremi dell'intervallo di lavoro

    tol: precisione richiesta

    it_max: numero massimo di iterate consentite

    Returns
    -------
    c: approssimazione di uno zero di f

    it: numero di iterate effettuate
    """

    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        print('la funzione non cambia di segno')
        return

    x0 = (a + b) / 2

    it = 0
    arresto = False
    while not arresto and it < it_max:
        it = it + 1

        fx0 = f(x0)
        x = x0 - m * fx0

        arresto = abs(x - x0) < tol
        x0 = x

    if not arresto:
        print('precisione non raggiunta')

    return x, it


def newton(f, x0, tol=1e-8, it_max=50):
    """
    METODO DI NEWTON
    Parameters
    ----------
    f: funzione di cui ricercare uno zero

    x0: stima iniziale dello zero alpha di f

    tol: precisione richiesta

    it_max: numero massimo di iterate consentite

    Returns
    -------
    c: approssimazione di uno zero di f

    it: numero di iterate effettuate
    """

    it = 0
    arresto = False
    while not arresto and it <= it_max:
        it = it + 1
        x1 = x0 - f(x0)/f(x0, 1)
        arresto = abs(x1 - x0) < tol
        x0 = x1


    if not arresto:
        print("Precisione non raggiunta")

    return x1, it


def newton_modificato(f, a, b, tol=1e-8, it_max=50):
    """
    METODO DELLA DIREZIONE COSTANTE

    Parameters
    ----------
    f: funzione di cui ricercare uno zero

    m: costante

    a,b: estremi dell'intervallo di lavoro

    tol: precisione richiesta

    it_max: numero massimo di iterate consentite

    Returns
    -------
    c: approssimazione di uno zero di f

    it: numero di iterate effettuate
    """

    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        print('la funzione non cambia di segno')
        return

    x0 = (a + b) / 2

    it = 0
    arresto = False
    while not arresto and it < it_max:
        it = it + 1
        x1 = x0 - f(x0)/f(x0, 1)
        arresto = abs(x1 - x0) < tol
        x0 = x1

    if not arresto:
        print('precisione non raggiunta')

    return x1, it


def secanti(f, x0, x1, tol=1e-8, it_max=50):
    arresto = False
    it = 0
    while not arresto and it < it_max:
        it = it + 1
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - (x1 - x0)/(fx1 - fx0) * fx1
        arresto = abs(x0 - x1) < tol

        x0 = x1
        x1 = x2

    if not arresto:
        print('Precisione non raggiunta')

    return x2, it


def f1(x, ord=0):
    if ord == 0:
        y = x - cos(x)
    elif ord == 1:
        y = 1 + sin(x)
    return y


def f2(x, ord=0):
    if ord == 0:
        y = x - exp(-x)
    elif ord == 1:
        y = 1 + exp(-x)
    return y