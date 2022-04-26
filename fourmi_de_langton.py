#################################
# Groupe MI TD2 (groupe de projet n°3)
# Tiphanie DEPREAUX
# Baptiste PARIS
# Ania AOUAOUCHE
# https://github.com/uvsq22102500/Fourmi-de-Langton

from tkinter import *

#--------------------------------------------------------------------------------------------------
# constantes 
#--------------------------------------------------------------------------------------------------
LARGEUR = 645
HAUTEUR = 645

N = 11 #(a modifier une fois que le programme fonctionne)

L = LARGEUR//N  #coté d'un carré de notre canvas

BLANC = 0
NOIR = 1

#directions possibles
NORD = 0
SUD = 1
WEST = 2
EST = 3

COULEUR_FLECHE = "blue"

#--------------------------------------------------------------------------------------------------
# variables globales 
#--------------------------------------------------------------------------------------------------

# liste 
grille = []
grille_canvas = []

# positions de la fourmi 
position_i = N//2
position_j = N//2

# direction de la fourmi 
DIRECTION = NORD

# creation de la fenetre principale 
window = Tk()
window.geometry("800x800")
window.title("Fourmi de Langton")
canvas = Canvas( window , height = HAUTEUR , width = LARGEUR )
frame = Frame (window , height = 100 , width = 100)
fleche = Canvas (window)

# -----------------------------------------------------------------------------------------------
# les fonctions
# -----------------------------------------------------------------------------------------------

# fonction d'initialisation

def initialisation(): 
    global grille, grille_canvas
    """initialisation de la grille a 0 """
    """cette grille nous permettra plus tard de savoir de quelle couleur est notre carré """
    """pour ensuite pouvoir la modifier (en 1 ou 0 ; 1 etant le noir ; 0 etant le blanc) """
    for i in range(N):
        grille.append([0]*N)
        grille_canvas.append([0]*N)

    """ une deuxieme grille a 2D pour la creation de notre environnement """ 
    """ une troisieme grille a 2D pour garder les coordonnées de nos carrés de notre environnement"""
    for i in range(N):
        for j in range(N):
            x, y = j*L , i*L #ca nous permet de nous positionner en fonction de i et de j
            carre = canvas.create_rectangle( (x,y), (x + L, y + L), fill="white")
            grille[i][j] = BLANC
            grille_canvas[i][j] = carre

# creation de notre fourmi "notre fleche"
def fourmi():
    global fleche

    x_mil = LARGEUR//2  #milieu de notre canvas en x
    y_mil = HAUTEUR//2  #milieu de notre canvas en y

    """verifier le cas ou le nombre de carrés est pair ou impair et placer la fleche au milieu"""
    if N%2 != 0 :
        x1 = x_mil 
        y1 = y_mil+ L/2
        x2 = x_mil
        y2 = y_mil- L/2
            
    else :
        x1 = x_mil + L/2
        y1 = y_mil + L
        x2 = x_mil + L/2
        y2 = y_mil 

    """creation de notre fleche initiale """    
    fleche = canvas.create_line ( (x1, y1), (x2, y2), fill = COULEUR_FLECHE, width = 5, smooth = True, arrow="last", arrowshape = (5,6,2) )
    
  
def fourmi_update():
    global fleche, position_i, position_j
    
    if DIRECTION == NORD:
        x1 = position_j * L + L/2   
        y1 = position_i *L + L
        x2 = position_j * L + L/2
        y2 = position_i *L 
        canvas.coords ( fleche , x1, y1, x2, y2 )

    elif DIRECTION == SUD:
        x2 = position_j * L + L/2   
        y2 = position_i *L + L
        x1 = position_j * L + L/2
        y1 = position_i *L 
        canvas.coords ( fleche , x1, y1, x2, y2 )
      
    elif DIRECTION == EST:
        x1 = position_j * L 
        y1 = position_i *L + L/2
        x2 = position_j * L + L 
        y2 = position_i *L + L/2
        canvas.coords ( fleche , x1, y1, x2, y2 )

    elif DIRECTION == WEST:
        x2 = position_j * L  
        y2= position_i *L + L/2
        x1 = position_j * L + L
        y1 = position_i *L + L/2
        canvas.coords ( fleche , x1, y1, x2, y2 )
    
   
        
        
def play ():
    global position_i, position_j , DIRECTION, grille , grille_canvas
    
    """verification de la couleur de notre carre"""

    if grille[position_i][position_j] == BLANC :
        grille[position_i][position_j] = NOIR 
        canvas.itemconfig( grille_canvas[position_i][position_j] ,  fill = "black")

        """changement de direction si la couleur du carré est blanc"""
        if DIRECTION == NORD:
            DIRECTION = EST
            position_j = (position_j+1)%N
            
        elif DIRECTION == SUD:
            DIRECTION = WEST
            position_j = (position_j-1)%N
            
        elif DIRECTION == EST:
            DIRECTION = SUD
            position_i = (position_i+1)%N
            
        elif DIRECTION == WEST:
            DIRECTION = NORD
            position_i = (position_i-1)%N
        
    else :
        grille[position_i][position_j] = BLANC 
        canvas.itemconfig( grille_canvas[position_i][position_j] ,  fill = "white")
        """changement de direction si la couleur du carré est noir"""
        if DIRECTION == NORD:
            position_j = (position_j-1)%N
            DIRECTION = WEST
            
        elif DIRECTION == SUD:
            position_j = (position_j+1)%N     
            DIRECTION = EST

        elif DIRECTION == EST:
            position_i = (position_i-1)%N
            DIRECTION = NORD

        elif DIRECTION == WEST:
            position_i = (position_i+1)%N
            DIRECTION = SUD
        
    fourmi_update()






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
fourmi()



window.mainloop()