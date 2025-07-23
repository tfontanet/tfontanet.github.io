from math import gcd

class Fraction:
    def __init__(self, n, d=1):
        """Constructeur qui génère une erreur si le dénominateur est nul, ou si n et d ne sont pas des entiers"""
        pass
    
    def __repr__(self):
        """Permet à Thonny et à Python de savoir comment représenter la fraction par exemple lors d'un print"""
        return str(self.numérateur)+"/"+str(self.dénominateur)

    def valeurdécimale(self):
        """Renvoie un flottant égal à la valeur décimale de la fraction""" 
        pass
    
    def pgcd(self):
        """Renvoie un entier égal au PGCD du numérateur et du dénominateur"""
        pass
    
    def simplifier(self):
        """Renvoie une fraction égale simplifiée sans modifier la fraction de départ"""
        pass
    
    def multiplier(self,other):
        """Renvoie une fraction égale au produit de cette fraction avec other"""
        pass
    
    def additionner(self,other):
        """Renvoie une fraction égale à la somme de cette fraction avec other"""
        pass
    

f1=Fraction(3,9)
print(f"{f1} = {f1.valeurdécimale()}")
print(f"Cette fraction est simplifiable par {f1.pgcd()} et une fois simplifiée s'écrit {f1.simplifier()}")
f2=Fraction(4,3)
print(f"{f1} + {f2} = {f1.additionner(f2)}")
print(f"{f1} × {f2} = {f1.multiplier(f2)}")
f3=Fraction(3,0)