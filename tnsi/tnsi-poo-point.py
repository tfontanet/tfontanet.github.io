from math import sqrt

class Point:
    def __init__(self, x, y):
        pass
        
    def __repr__(self):
        """Permet à Thonny et à Python de savoir comment représenter le point par exemple lors d'un print"""
        pass 

    def distance(self, other):
        """Renvoie un float donnant la distance entre ce point et le point "other" """
        pass
    
    def milieu(self, other):
        """Renvoie un point qui est le milieu du segment d'extrémités le point courant et "other" """
        pass
    
    def déplacer(self, dx, dy):
        """Déplace le point de dx en abscisse et de dy en ordonnée"""
        pass
        
        

A = Point(4,-1)
B = Point(4, 3)
print(f"La distance entre A et B est {A.distance(B)}")
print(f"et le milieu est le point {A.milieu(B)}")
A.déplacer(2, 3)

