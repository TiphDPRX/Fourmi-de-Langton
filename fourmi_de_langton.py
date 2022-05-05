#################################
# Groupe MI TD2 (groupe de projet n°3)
# Tiphanie DEPREAUX
# Baptiste PARIS
# Ania AOUAOUCHE
# https://github.com/uvsq22102500/Fourmi-de-Langton

from tkinter import *
from threading import Timer
import time

#-------------------------------------------------------------------------------------------------------
# constantes 
#-------------------------------------------------------------------------------------------------------

# dimensions de notre canvas
LARGEUR = 640
HAUTEUR = 640

# nombre et dimensions des carrés de notre canvas
N = 15
L = LARGEUR//N   

#couleurs possibles
BLANC = 0
NOIR = 1

COULEUR_FLECHE = "blue"
 
#directions possibles de la fleche
NORD = 0
SUD = 1
WEST = 2
EST = 3

#-------------------------------------------------------------------------------------------------------
# variables globales 
#-------------------------------------------------------------------------------------------------------

# listes
grille = []
grille_canvas = []

# positions de la fourmi 
position_i = N//2
position_j = N//2

# direction initiale de la fourmi 
DIRECTION = NORD

# variable qui nous permettra de mettre le buton play en pause
mouv = True

# creation de la fenetre principale ---------------------------------------------------------------
window = Tk()
window.geometry("1000x700")
window.title("Fourmi de Langton")
window.configure(background='white')

#creation d'un canvas pour generer notre terrain
canvas = Canvas( window , height = HAUTEUR , width = LARGEUR, background='white' )

#creation de notre fleche
fleche = Canvas (window)

#creation d'une boite ou on mettra nos boutons 
frame = Frame (window, height = 320 , width = 360)

#implementer une image 
canvas_image = Canvas (window, height = 320 , width = 360)
image = PhotoImage(file='clavier.gif')
label= Label (canvas_image,image = image)

# -----------------------------------------------------------------------------------------------
# les fonctions
# -----------------------------------------------------------------------------------------------

# --------------------- fonction d'initialisation ---------------------

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

#--------------------- creation de notre fourmi "notre fleche" ---------------------
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
    
#---------------------fonction qui permet de changer les coordonnés de la fleche ,"sa position"-----------------
def fourmi_update():
    global fleche, position_i, position_j, id_after

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

    id_after = canvas.after(1000, play)
    
#---------------------fonction qui permet de changer la couleur d'un carré et de changer la direction de la fleche--
def play ():
    global position_i, position_j , DIRECTION, grille , grille_canvas
    
    """verification de la couleur de notre carre"""
    if grille[position_i][position_j] == BLANC :
        grille[position_i][position_j] = NOIR 
        canvas.itemconfigure( grille_canvas[position_i][position_j] ,  fill = "black")

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
        canvas.itemconfigure(grille_canvas[position_i][position_j], fill = "white")

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

#--------------fonction qui change le bouton "play" en bouton "pause",et active la fonction play-------------
def demarrer ():
    global mouv, id_after

    if mouv:
        button_play.config(text="Pause")
        play()
    else:
        canvas.after_cancel(id_after)
        button_play.config(text="Play")

    mouv = not mouv #ici, on utilise "not" et non "false" pour avoir tjs le contraire de mouv    

#------------------ fonction qui permet d'enregistrer une sequence dans un fichier -------------------------
def enregistre():
    """Ecrit la taille de la grille et les valeurs de la liste
    grille dans le fichier enregistrement.txt"""
    
    fic = open("enregistrement.txt", "w")
    fic.write(str(N) + "\n")
    fic.write(str(position_i)+ "\n")
    fic.write(str(position_j)+ "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(grille[i][j])+ "\n")

    fic.close()

#------------------ fonction qui permet de lire le fichier et affiche dans le canvas la grille lu ----------------
def charge_grille():
    global N, position_i, position_j

    fic = open("enregistrement.txt", "r")

    taille = fic.readline()
    position1 = fic.readline()
    position2 = fic.readline()

    N = int(taille)
    position_i = int(position1)
    position_j = int(position2)
    canvas.delete()
    
    initialisation() # initialisation pour avoir des listes à la bonne taille
    i , j =0, 0
    for ligne in fic:
        grille[i][j] = int(ligne)
        j += 1
        if j == N:
            j = 0
            i += 1
    print(grille)
    for i in range(N):
        for j in range(N):
            if grille[i][j]== 0:
                canvas.itemconfigure(grille_canvas[i][j], fill = "white")
            elif grille[i][j]==1:  
                canvas.itemconfigure(grille_canvas[i][j], fill = "black")
    fourmi()
    demarrer()
    fic.close()

#fonction qui permet d'accelerer le mouvement de la fourmi------------------------------------------------
def leftKey (event):
    pass
    
#fonction qui permet de ralentir le mouvement de la fourmi------------------------------------------------
def rightKey (event):
    pass
    
window.bind ('<Right>', rightKey)
window.bind ('<Left>', leftKey)

def next ():
    pass

# ---------- fonction qui permet de revenir en arriere d'un mouvement -----------------------------------
def retour ():
    global DIRECTION, grille,position_i, position_j

    if DIRECTION == NORD :
        if grille[position_i+1][position_j] == BLANC :
            grille[position_i+1][position_j] = NOIR
            canvas.itemconfig( grille_canvas[position_i+1][position_j] ,  fill = "black")
            position_i = (position_i+1)%N
            DIRECTION = EST
        else :
            grille[position_i+1][position_j] = BLANC
            canvas.itemconfig( grille_canvas[position_i+1][position_j] ,  fill = "white")
            position_i = (position_i+1)%N
            DIRECTION = WEST

    elif DIRECTION == SUD :
        if grille[position_i-1][position_j] == BLANC :
            grille[position_i-1][position_j] = NOIR
            canvas.itemconfig( grille_canvas[position_i-1][position_j] ,  fill = "black")
            position_i = (position_i-1)%N
            DIRECTION = WEST
        else :
            grille[position_i-1][position_j] = BLANC
            canvas.itemconfig( grille_canvas[position_i-1][position_j] ,  fill = "white")
            position_i = (position_i-1)%N
            DIRECTION = EST
            
    elif DIRECTION == EST :
        if grille[position_i][position_j-1] == BLANC :
            grille[position_i][position_j-1] = NOIR
            canvas.itemconfig( grille_canvas[position_i][position_j-1] ,  fill = "black")
            position_j = (position_j-1)%N
            DIRECTION = SUD
        else :
            grille[position_i][position_j-1] = BLANC
            canvas.itemconfig( grille_canvas[position_i][position_j-1] ,  fill = "white")
            position_j = (position_j-1)%N
            DIRECTION = NORD

    elif DIRECTION == WEST :
        if grille[position_i][position_j+1] == BLANC :
            grille[position_i][position_j+1] = NOIR
            canvas.itemconfig( grille_canvas[position_i][position_j+1] ,  fill = "black")
            position_j = (position_j+1)%N
            DIRECTION = NORD
        else :
            grille[position_i][position_j+1] = BLANC
            canvas.itemconfig( grille_canvas[position_i][position_j+1] ,  fill = "white")
            position_j = (position_j+1)%N
            DIRECTION = SUD
    mouv = True
    fourmi_update()


# les boutons --------------------------------------------------------------------------
button_play = Button (frame , text = ' Play  ', command = demarrer ) 
button_play.pack(padx= 10 , pady=10 )
Button (frame , text = ' Next ', command = next).pack(padx= 10 , pady=10 )
Button (frame , text = 'Return', command = retour).pack(padx= 10 , pady=10 )
Button(frame, text="Enregistre", command=enregistre).pack(padx= 10 , pady=10 )
Button(frame, text="Charger grille", command=charge_grille).pack(padx= 10 , pady=10 )

# affichage------------------------------------------------------------------------------
canvas.pack (side = RIGHT)
frame.place ( x=150 , y=50)
canvas_image.place( x=30 , y= 350)
label.pack()

initialisation()
fourmi()

window.mainloop()