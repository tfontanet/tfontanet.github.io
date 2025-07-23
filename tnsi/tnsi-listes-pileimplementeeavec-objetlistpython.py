# Objectif : Implémenter une pile en s'appuyant sur l'objet list Python
# On pourra utiliser ci-dessous les méthodes append et pop

class Pile:
    def __init__(self):
        self.pile=[]

    def est_vide(self):
        pass
    
    def empiler(self,valeur):
        pass
        
    def lire_sans_dépiler(self):
        pass
    
    def dépiler(self):
        pass
    
    def __repr__(self):
        return str(self.pile)


# Création de la pile
a=Pile()
assert a.est_vide()
a.empiler(5)
assert not a.est_vide()
a.empiler(6)
assert a.lire_sans_dépiler() == 6
a.empiler(10)
a.empiler(11)
a.empiler(12)
assert a.dépiler() == 12
assert a.dépiler() == 11
assert a.dépiler() == 10
assert a.dépiler() == 6
assert a.dépiler() == 5
assert a.est_vide()
