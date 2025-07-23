class Rectangle:
    def __init__(self,a,b):
        """Constructeur.
        Vérifie que a et b sont des nombres positifs
        La longueur doit être le plus grand côté"""
        pass
        
    def __repr__(self):
        return f"Rectangle {self.longueur} x {self.largeur}"

    def aire(self):
        """renvoie l'aire du rectangle"""
        pass
    
    def périmètre(self):
        """renvoie le périmètre du rectangle"""
        pass
    
    def est_carré(self):
        """renvoie True si le rectangle est carré et False sinon"""
        pass
    
r1=Rectangle(2,5)
print(f"Le rectangle de longueur {r1.longueur} et de largeur {r1.largeur} a pour aire {r1.aire()}")
if r1.est_carré():
    print("et en plus, c'est un carré !")
r2=Rectangle(3,3)
print(f"Le rectangle de longueur {r2.longueur} et de largeur {r2.largeur} a pour aire {r2.aire()}")
if r2.est_carré():
    print("et en plus, c'est un carré !")
r3=Rectangle(4,4)
if r3.périmètre() == r3.aire():
    print(f"Le rectangle de longueur {r3.longueur} et de largeur {r3.largeur} a son périmètre égal à son aire !")
