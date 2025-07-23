# Objectif : Implémenter une liste sans s'appuyer sur l'objet list Python
# Nous n'utiliserons ni "self.liste = []", ni les fonctions et méthodes "len", "append", "pop",...
# En revanche, nous nous appuyerons sur la classe Maillon ci-dessous.

class Maillon:
    def __init__(self, valeur, maillon_suivant = None):
        self.valeur = valeur
        self.suivant = maillon_suivant
    
    def __repr__(self):
        return f"{self.valeur}->{self.suivant}"

class Liste:
    def __init__(self):
        self.début = None
    
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
        if self.début == None:
            return "None"
        else:
            return f"{self.début}"


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

# Remarque, nous avons implémenté notre liste chainée ci-dessus à l'aide de deux classes : Maillon et Liste.
# Nous aurions pu faire un autre choix et nous contenter de la classe Maillon mais c'est moins pratique ensuite (cf code ci-dessous ;-)
tête_liste = Maillon(5, Maillon(2, Maillon(3)))
print(tête_liste)
tête_liste.suivant = Maillon(10, tête_liste.suivant)
print(tête_liste)

