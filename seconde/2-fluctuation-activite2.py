from random import randint
from pylab import plot, axis, show
from math import sqrt, fabs

def RésultatChute():
    somme = 0
    for i in range(3):
        rebond = randint(0, 1)
        somme = somme + rebond
    return somme

def Echantillon(n, numéro):
    s = 0
    for i in range(n):
        if RésultatChute() == numéro:
            s = s + 1
    p = s/n
    return p

def Graphique(numéro):
    taille = 1000
    for i in range(100):
        f = Echantillon(taille, numéro)
        plot(i, f, 'x', color='red')
    axis([0, 100, 0, 1])
    show()

def Erreur(n, numéro):
    nb = 0
    proba = [1/8, 3/8, 3/8, 1/8]
    for i in range(100):
        f = Echantillon(n, numéro)
        e = fabs(f - proba[numéro])
        if e <= 1/sqrt(n):
            nb = nb + 1
    return nb
