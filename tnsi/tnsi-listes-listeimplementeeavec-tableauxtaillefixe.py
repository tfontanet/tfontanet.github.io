# Objectif : Implémenter une liste en utilisant un tableau de taille fixe.
# Ce tableau sera une liste Python, mais nous n'utiliserons ci-dessous aucune des méthodes et fonctions associées
# aux listes Python : Pas de append, pop, insert, len,...
# Le but est de programmer nous même le décalage des valeurs dans le tableau quand on veut ajouter ou supprimer
# un élément de la liste.
# A la création d'un objet de classe "Liste" ci-dessous, on définira la taille du tableau à créer
# et on appelera "imax" l'indice du dernier élément utilisé.

class Liste:
    def __init__(self, taille):
        self.taille = taille
        self.tableau = [0]*taille
        self.imax = -1
    
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
        return str(self.tableau) + ", imax = " + str(self.imax)


a=Liste(5)
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