# Objectif : Implémenter une liste en s'appuyant sur l'objet list Python

class Liste:
    def __init__(self):
        self.liste = []
    
    def est_vide(self):
        pass
    
    def longueur(self):
        pass
    
    def ajouter(self, valeur, indice=0):
        pass
        
    def supprimer(self, indice=0):
        pass
        
    def lire(self, indice):
        pass
        
    def __repr__(self):
        return str(self.liste)
    
a=Liste()
assert a.est_vide()
assert a.longueur() == 0
a.ajouter(2,0)
assert not a.est_vide()
assert a.longueur() == 1
a.ajouter(5,0)
assert a.longueur() == 2
a.ajouter(3,2)
assert a.longueur() == 3
print(a)
a.supprimer(1)
assert a.longueur() == 2
print(a)
assert a.lire(0) == 5
assert a.lire(1) == 3