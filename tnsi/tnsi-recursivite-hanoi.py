# Tours de Hanoi avec tkinter
# Adapté de https://github.com/erdc/python/blob/master/Demo/tkinter/guido/hanoi.py

########################################
# Ne pas modifier cette partie du code #
########################################
from tkinter import *
import time

def dessine_tours(n):
    # Création de l'interface graphique
    global tk, canvas, pegs, pegstate, pieces

    tk = Tk()
    canvas = Canvas(tk)
    canvas.pack()
    width, height = tk.getint(canvas['width']), tk.getint(canvas['height'])

    # Dessin des tours
    pegwidth = 10
    pegheight = height//2
    pegdist = width//3
    x1, y1 = (pegdist-pegwidth)//2, height*1//3
    x2, y2 = x1+pegwidth, y1+pegheight
    pegs = []
    p = canvas.create_rectangle(x1, y1, x2, y2, fill='black')
    pegs.append(p)
    x1, x2 = x1+pegdist, x2+pegdist
    p = canvas.create_rectangle(x1, y1, x2, y2, fill='black')
    pegs.append(p)
    x1, x2 = x1+pegdist, x2+pegdist
    p = canvas.create_rectangle(x1, y1, x2, y2, fill='black')
    pegs.append(p)
    tk.update()

    # Variable qui contient l'état du jeu :
    pegstate = [[], [], []]

    # Dessin des disques
    pieceheight = pegheight//16
    maxpiecewidth = pegdist*2//3
    minpiecewidth = 2*pegwidth
    pieces = {}
    x1, y1 = (pegdist-maxpiecewidth)//2, y2-pieceheight-2
    x2, y2 = x1+maxpiecewidth, y1+pieceheight
    dx = (maxpiecewidth-minpiecewidth) // (2*max(1, n-1))
    for i in range(n, 0, -1):
        p = canvas.create_rectangle(x1, y1, x2, y2, fill='red')
        pieces[i] = p
        pegstate[0].append(i)
        x1, x2 = x1 + dx, x2-dx
        y1, y2 = y1 - pieceheight-2, y2-pieceheight-2
        tk.update()
        tk.after(25)
    print(pegstate)

def déplacer_un_disque(départ, arrivée):
    assert len(pegstate[départ]) >= 1, f"Erreur : pas de disque à déplacer sur la tour {départ} !"
    if len(pegstate[arrivée]) >= 1:
        assert pegstate[départ][-1] < pegstate[arrivée][-1], f"Erreur : le disque de la tour {départ} est trop grand pour aller sur la tour {arrivée} !"
    time.sleep(1)
    i = pegstate[départ][-1]
    del pegstate[départ][-1]
    p = pieces[i]

    # Fait sortir le disque de la tour de départ
    ax1, ay1, ax2, ay2 = canvas.bbox(pegs[départ])
    x1, y1, x2, y2 = canvas.bbox(p)
    while ay1 <= y2:
        y2 -= 1
        canvas.move(p, 0, -1)
        tk.update()
        time.sleep(0.0005)

    # Déplace le disque vers la tour d'arrivée
    bx1, by1, bx2, by2 = canvas.bbox(pegs[arrivée])
    newcenter = (bx1+bx2)//2
    x1, y1, x2, y2 = canvas.bbox(p)
    center = (x1+x2)//2
    while center != newcenter:
        if center > newcenter:
            canvas.move(p, -1, 0)
            center -= 1
        else:
            canvas.move(p, 1, 0)
            center += 1
        tk.update()
        time.sleep(0.0005)

    # Insère le disque sur la tour d'arrivée
    pieceheight = y2-y1
    newbottom = by2 - pieceheight*len(pegstate[arrivée]) - 2
    x1, y1, x2, y2 = canvas.bbox(p)
    while newbottom > y2:
        canvas.move(p, 0, 1)
        newbottom -= 1
        tk.update()
        time.sleep(0.0005)

    # Met à jour la variable pegstate qui contient l'état du jeu
    pegstate[arrivée].append(i)
    print(pegstate)

    


##############################################
# Mode d'emploi et Partie du code à modifier #
##############################################
# Les tours sont numérotées 0, 1 et 2. Au départ les disques sont sur la tour 0
# La fonction "dessine_tours(n)" permet d'initialiser une partie avec n disques sur la tour de départ
# La fonction "déplacer_un_disque(a,b)" déplace le disque au sommet de la tour a vers le sommet de la tour b
#
# A faire :
# 1. tester le code ci-dessous pour bien comprendre l'utilisation des fonctions "dessine_tours(n)" et "déplacer_un_disque(a,b)"
# 2. compléter le code de la fonction récursive "hanoi" pour qu'elle puisse terminer la partie automatiquement.

def hanoi(nbre_disques_à_déplacer, départ, arrivée, intermédiaire):
    pass



dessine_tours(3) 
déplacer_un_disque(0,2)
déplacer_un_disque(0,1)
déplacer_un_disque(2,1)
déplacer_un_disque(0,2)
déplacer_un_disque(1,0)
déplacer_un_disque(1,2)
déplacer_un_disque(0,2)


# hanoi(3, 0, 2, 1)
