

from tkinter import *
from tkinter.messagebox import showinfo
import random



# ----- Fonctions : -----

def afficher_confirmation() :
    """fonction créant une petite interface graphique confirmant l'achat"""

    showinfo("Confirmation de l'achat",
             "Vous avez bien fait l'acquisition de vos actions")


def ouvrir() :
    """création d'une nouvelle interface pour l'achat d'actions"""

    fen = Tk()
    fen.title("Achat des actions")

    explication = Label(fen, text = "Nombre d'actions souhaitées : ")

    actions = IntVar()

    champ = Entry(fen, textvariable = actions)
    champ.focus_set()
    
    bouton = Button(fen, text = 'Valider', command = afficher_confirmation)

    # disposition de tous les widgets créés à l'aide de la méthode grid()
    explication.grid(row = 1, column = 1, padx = 10, pady = 10)
    champ.grid(row = 1, column = 2, padx = 10, pady = 10)
    bouton.grid(row = 1, column = 3, padx = 10, pady = 10)
    
    fen.mainloop()
    
    return actions.get() # idée : envoyer à une fonction stocker
    

def tracer_segments() :
    """fonction qui permet le tracé d'un segment aléatoire"""

    global pt
    global T
    
    x_1 = pt[0] + T*10
    y_1 = pt[1] + random.randint(-10,10)
    
    # utilisation de la méthode create_line() appliquée à l'objet canevas :
    canevas.create_line(pt[0], pt[1], x_1, y_1, fill = 'blue')
    
    pt = (x_1, y_1) # mise à jour du point d'arrivée d'où on repartira

    # utilisation de la méthode after() appliquée à l'objet fenetre.
    # Elle permet d'exécuter une action après un temps donné en ms.
    fenetre.after(T*1000, tracer_segments)


def tracer_axes(T) :
    """trace le repère en fonction de la période puis fait appel
    à la fonction tracer_segment"""

    # affichage des axes :

    # axe des abscisses
    canevas.create_line(5, 390, 995, 390, arrow = LAST)
    # axe des ordonnées
    canevas.create_line(10, 395, 10, 10, arrow = LAST)

    # graduation des axes :

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
    démarrer. Permet le démarrage du tracé (des axes et de la courbe)."""

    global T
    tracer_axes(T)
    tracer_segments()


# ----- Procédure : -----

pt = (10, 200)

T = int(input("Période souhaitée (en s) : "))

fenetre = Tk()
fenetre.title("Cours de l'action")

# initialisation de l'objet canevas à partir de la classe Canvas() :
canevas = Canvas(fenetre, width = 1000, height = 400, bg = 'white')
# affichage :
canevas.grid(row = 1, column = 1, rowspan = 3, padx = 10, pady = 10)

# initialisation d'objets de classe Button() :
bouton1 = Button(fenetre, text = 'Démarrer', command = demarrer)
bouton2 = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
bouton3 = Button(fenetre, text = 'Acheter des actions', command = ouvrir)
# affichage :
bouton1.grid(row = 1, column = 2, padx = 10, pady = 10)
bouton2.grid(row = 3, column = 2, padx = 10, pady = 10)
bouton3.grid(row = 2, column = 2, padx = 10, pady = 10) 

# démarrage du réceptionnaire d'évènements associé à la fenêtre
fenetre.mainloop()
