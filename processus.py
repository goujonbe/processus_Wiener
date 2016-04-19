

from tkinter import *
import random

def tracer_segments() :
    """fonction qui permet le tracé d'un segment aléatoire"""

    global pt
    global T
    
    x_1 = pt[0] + T*10
    y_1 = pt[1] + random.randint(-10,10)
    
    canevas.create_line(pt[0], pt[1], x_1, y_1)
    pt = (x_1, y_1)

    fenetre.after(T*1000, tracer_segments)


        
    

def tracer_axes(T) :
    """trace le repère en fonction de la période puis fait appel
    à la fonction tracer_segment"""

    # affichage des axes :

    # axe des abscisses
    canevas.create_line(5, 390, 995, 390, arrow = LAST)
    # axe des ordonnées
    canevas.create_line(10, 395, 10, 10, arrow = LAST)

    # graduation des axes

    # axe des abscisses (en fonction de la période T)
    abscisse = 10
    while abscisse <= 985 :
        canevas.create_line(abscisse, 388, abscisse, 392)
        abscisse = abscisse + T*10

    # axe des ordonnées
    ordonnee = 30
    while ordonnee <= 390 :
        canevas.create_line(8, ordonnee, 12, ordonnee)
        ordonnee = ordonnee + 20

    
        



def demarrer() :
    """fonction répondant à l'utilisateur lorsqu'il appuie sur le bouton
    démarrer. Permet le démarrage du tracé."""

    global T
    tracer_axes(T)
    tracer_segments()


pt = (10, 200)

T = int(input("Période souhaitée (en s) : "))

fenetre = Tk()
fenetre.title("Cours de l'action")

canevas = Canvas(fenetre, width = 1000, height = 400, bg = 'white')
canevas.grid(row = 1, column = 1, rowspan = 3, sticky = W, padx = 10, pady = 10)

bouton1 = Button(fenetre, text = 'Démarrer', command = demarrer)
bouton2 = Button(fenetre, text = 'Quitter', command = fenetre.destroy)

bouton1.grid(row = 1, column = 2, padx = 10, pady = 10)
bouton2.grid(row = 3, column = 2, padx = 10, pady = 10)

fenetre.mainloop()
