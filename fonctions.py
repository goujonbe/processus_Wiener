
from tkinter import *
import random



def tracer_segments(T) :
    """trace un segment aléatoire"""

    global pt

    # affichage des axes :

    # axe des abscisses
    canevas.create_line(5, 390, 390, 390, arrow = LAST)
    # axe des ordonnées
    canevas.create_line(10, 395, 10, 10, arrow = LAST)

    # graduation des axes

    # axe des abscisses (en fonction de la période T)
    abscisse = 10
    while abscisse <= 380 :
        canevas.create_line(abscisse, 388, abscisse, 392)
        abscisse = abscisse + T

    # axe des ordonnées
    ordonnee = 30
    while ordonnee <= 390 :
        canevas.create_line(8, ordonnee, 12, ordonnee)
        ordonnee = ordonnee + 20

    for i in range (0,200) :

        x_1 = pt[0] + T
        y_1 = pt[1] + random.randint(-10,10)
        
        canevas.create_line(pt[0], pt[1], x_1, y_1)
        pt = (x_1, y_1)

def demarrer() :
    """fonction répondant à l'utilisateur lorsqu'il appuie sur le bouton
    démarrer. Permet le démarrage du tracé."""
  
    global T
    tracer_segments(T)


pt = (10, 200)

T = int(input("Période souhaitée : "))

fenetre = Tk()
fenetre.title("Processus de Wiener")

canevas = Canvas(fenetre, width = 400, height = 400, bg = 'white')
canevas.grid(row = 1, column = 1, rowspan = 3, sticky = W, padx = 10, pady = 10)

bouton1 = Button(fenetre, text = 'Démarrer', command = demarrer)
bouton2 = Button(fenetre, text = 'Quitter', command = fenetre.destroy)

bouton1.grid(row = 1, column = 2, padx = 10, pady = 10)
bouton2.grid(row = 3, column = 2, padx = 10, pady = 10)

fenetre.mainloop()
