#################################
# Groupe MI TD2 (groupe de projet n°3)
# Tiphanie DEPREAUX
# Baptiste PARIS
# Ania AOUAOUCHE
# https://github.com/uvsq22102500/Fourmi-de-Langton

from tkinter import *

# constantes -----------------------------------------------------------------
H = 500
W = 500

N = 500


# creation de la fenetre principale ------------------------------------------
window = Tk()
window.geometry("600x600")
canvas = Canvas( window , height = H , width = W )
''' changer l'icone en fourmi '''
frame = Frame (window , height = 100 , width = 100 )

# creation de la grille ------------------------------------------------------
for i in range (N):
    for j in range (N):
        canvas.create_rectangle( (10*i , 10*j) , ( (10*(i+1)) , (10*(j+1)) ) , fill='white')


# les fonctions ---------------------------------------------------------------
def play ():
    pass

def pause ():
    pass

def next ():
    pass

def retour ():
    pass

# les bouttons -----------------------------------------------------------------
button_play = Button (frame , text = 'Play', bg = 'black' , fg = 'white', command = play ) 
button_pause = Button (frame , text = 'Pause', bg = 'black' , fg = 'white', command = pause )
button_next = Button (frame , text = 'Next', bg = 'black' , fg = 'white', command = next)
button_return = Button (frame , text = 'Retrun', bg = 'black' , fg = 'white', command = retour)


# affichage----------------------------------------------------------------------
canvas.pack (side = TOP)
frame.pack (side = BOTTOM )

button_play.grid (row = 0, column =0)
button_pause.grid (row = 0, column =1)
button_next.grid (row = 1, column =0)
button_return.grid (row = 1, column =1)

window.mainloop()