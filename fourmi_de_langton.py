#################################
# Groupe MI TD2 (groupe de projet n°3)
# Tiphanie DEPREAUX
# Baptiste PARIS
# Ania AOUAOUCHE
# https://github.com/uvsq22102500/Fourmi-de-Langton

from tkinter import *

# constantes -----------------------------------------------------------------
H = 700 #canvas
W = 700 # canvas
LARGEUR = 645 # 43*15 il nous faut un nombre de carré impair sur la largeur
HAUTEUR = 645

N = 43

# variables globales ------------------------




# liste ---------------------
grille = []



# creation de la fenetre principale ------------------------------------------
window = Tk()
window.geometry("800x800")
window.title("Fourmi de Langton")
canvas = Canvas( window , height = HAUTEUR , width = LARGEUR )
''' changer l'icone en fourmi '''
frame = Frame (window , height = 100 , width = 100)


# les fonctions ---------------------------------------------------------------

def initialisation():
    """Initialise la grille blanche et chaque carre de la grille aura son identifiant enregistre dans la liste grille"""    
    # Cette liste "grille" à deux dimensions permet d'associer une valeur à chaque carré qui sera crée par la suite par la variable "carre",
    # On pourra alors agir sur chaque carre de manière individuel
    for i in range(N):
        grille.append([0]*N)

    #Création des carrés
    for i in range(N):
        for j in range(N):
            carre = canvas.create_rectangle(LARGEUR//N*i, HAUTEUR//N*j,LARGEUR//N*(i+1), HAUTEUR//N*(j+1), fill = "white")
            grille[i][j] = carre

def initialisation():
    """Initialise la grille blanche et chaque carre de la grille aura son identifiant enregistre dans la liste grille"""    
    # Cette liste "grille" à deux dimensions permet d'associer une valeur à chaque carré qui sera crée par la suite par la variable "carre",
    # On pourra alors agir sur chaque carre de manière individuel
    for i in range(N):
        grille.append([0]*N)

    #Création des carrés
    for i in range(N):
        for j in range(N):
            carre = canvas.create_rectangle(LARGEUR//N*i, HAUTEUR//N*j,LARGEUR//N*(i+1), HAUTEUR//N*(j+1), fill = "white", outline = "black")
            grille[i][j] = carre

def coul_carre(x, y):
    """définit la couleur du carré lorsque la fourmi le quitte"""
    canvas.itemconfigure(grille[x][y], fill = "white")

def fourmi():
    global triangle, x1, y1, x2, y2, x3, y3, l, h
    x_mil = LARGEUR//2
    y_mil = HAUTEUR//2
    l = LARGEUR//N
    h = HAUTEUR//N
    x1 = x_mil-1/2*l
    y1 = y_mil-1/2*h
    x2 = x_mil-1/2*l
    y2 = y_mil+1/2*h
    x3 = x_mil+1/2*l
    y3 = y_mil
    triangle = canvas.create_polygon((x1, y1, x2, y2, x3, y3), fill = "red")
    



def play ():
    pass

def pause ():
    pass

def next ():
    pass

def retour ():
    pass


# les boutons -----------------------------------------------------------------
button_play = Button (frame , text = ' Play  ', command = play ) 
button_pause = Button (frame , text = ' Pause', command = pause )
button_next = Button (frame , text = ' Next ', command = next)
button_return = Button (frame , text = 'Return', command = retour)


# affichage----------------------------------------------------------------------
canvas.pack (side = TOP)
frame.pack (side = BOTTOM )

button_play.grid (row = 0, column =0)
button_pause.grid (row = 0, column =1)
button_next.grid (row = 1, column =0)
button_return.grid (row = 1, column =1)

initialisation()
fourmi()



window.mainloop()