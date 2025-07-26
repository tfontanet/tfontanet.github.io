# Prérequis : La bibliothèque pillow doit être installée (bibliothèque de traitement d'images pour Python)
#             Et il faut avoir téléchargé l'image "eiffel.gif"
# A faire :
# 1) Copier-coller les fonctions écrites dans l'activité précédentes, puis les adapter à une image :
#    img.getpixel( (23, 45) ) permet de retourner un tuple contenant la couleur du pixel de coordonnées (23, 45)
#    img.putpixel( (23, 45), (100, 100, 100) ) permet d'affecter la couleur grise (100, 100, 100) au pixel de coordonnées (23, 45)
# 2) Pourquoi la tour Eiffel tourne vers la gauche au lieu de tourner vers la droite comme tout à l'heure ?


def permute_quadrants(img, quadrant_1, quadrant_2, n):
    """
    Échange les contenus de deux quadrants carrés de taille n x n.
    Ces quadrants sont définis par les coordonnées du coin en haut à gauche et par leur largeur.
    Paramètres :
        img : Image carrée
        quadrant_1 : Tuple donnant les coordonnées du coin en haut et à gauche du quadrant 1
        quadrant_2 : Tuple donnant les coordonnées du coin en haut et à gauche du quadrant 2
        n : Entier positif donnant la largeur des deux cadrants
    Valeur renvoyée :
        Ne renvoie rien mais modifie le tableau donné en entrée
    """
    pass


def tourne_recursif(img, carré, n):
    """
    Découpe un carré de taille n x n en 4 quadrants, puis fait faire à ces quadrants un quart de tour dans le sens horaire :
         ┌───┬───┐                        ┌───┬───┐     
         │ A │ B │                        │ D │ A │    
    Ex : ├───┼───┤ devient après rotation ├───┼───┤
         │ D │ C │                        │ C │ B │  
         └───┴───┘                        └───┴───┘      
    Puis la fonction s'appelle récursivement pour chacun des quadrants qui sont à leur tour découpés en 4...
    Le carré de départ est défini par les coordonnées du coin en haut à gauche et par sa largeur.
    Paramètres :
        img : Image carrée
        carré : Tuple donnant les coordonnées du coin en haut à gauche du cadrant
        n : Entier positif donnant la largeur du carré de départ. (n doit être une puissance de 2)
    Valeur renvoyée :
        Ne renvoie rien mais modifie le tableau donné en entrée
    """
    pass


# Exécution de l'algorithme sur une image
from PIL import Image

img = Image.open("eiffel.gif")
img.show()
tourne_recursif(img, (0, 0), img.width)
img.show()

