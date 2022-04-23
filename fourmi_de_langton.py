#################################
# Groupe MI TD2 (groupe de projet n°3)
# Tiphanie DEPREAUX
# Baptiste PARIS
# Ania AOUAOUCHE
# https://github.com/uvsq22102500/Fourmi-de-Langton

from tkinter import *

# constantes -----------------------------------------------------------------
LARGEUR = 500
HAUTEUR = 500

N = 48

# variables globales ------------------------


# liste ---------------------
grille = []



# creation de la fenetre principale ------------------------------------------
window = Tk()
window.geometry("600x600")
window.title("Fourmi de Langton")
canvas = Canvas( window , height = HAUTEUR , width = LARGEUR )
frame = Frame (window , height = 100 , width = 100)
''' changer l'icone en fourmi '''


# les fonctions ---------------------------------------------------------------

def initialisation():
    """Initialise la grille blanche et enregistre l'identifiant de chaque carre dans la liste"""    
    # Cette liste "grille" à deux dimensions permet d'associer une valeur à chaque carré qui sera crée par la suite par la variable "carre",
    # On pourra alors agir sur chaque carre de manière individuel
    for i in range(N):
        grille.append([0]*N)

    #Création des carrés
    for i in range(N):
        for j in range(N):
            carre = canvas.create_rectangle(LARGEUR//N*i, HAUTEUR//N*j,LARGEUR//N*(i+1), HAUTEUR//N*(j+1), fill = "white")
            grille[i][j] = carre

def fourmi(x, y):
    """Initialise la fourmi (temporaire qui sera un carré) au milieu du canevas"""
    canvas.itemconfigure(grille[x][y], fill = "blue")
            


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

# creation de notre "fourmi"



# affichage----------------------------------------------------------------------
canvas.pack (side = TOP)
frame.pack (side = BOTTOM )

button_play.grid (row = 0, column =0)
button_pause.grid (row = 0, column =1)
button_next.grid (row = 1, column =0)
button_return.grid (row = 1, column =1)

initialisation()
fourmi(N//2, N//2)



window.mainloop()