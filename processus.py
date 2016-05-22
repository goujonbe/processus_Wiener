
# --*-- coding : utf-8 --*--

from tkinter import *
from tkinter.messagebox import showinfo
import fonctions
import random


# ----- Fonctions : -----

def effacer() :
    """fonction qui permet l'arrêt du tracé de la courbe et efface le tracé"""

    global arret
    global y
    arret = True

    canevas.delete(ALL)
    barre_notifs.delete(ALL)
    y = 10

    
def Apropos() :
    """fonction créant une petite fenêtre avec des explications sur
    le projet"""
    showinfo("A propos",
             "Le projet est une simulation autour de la finance")

def personnaliser() :
    """ouverture d'une interface permettant de changer beaucoup de paramètres"""
    fen4 = Tk()

    fen4.mainloop()
    

def maj_periode(nouvelle_periode) :
    """fonction exécutée à chaque changement de position du curseur"""
    global T
    T = int(nouvelle_periode)

    
def acheter() :
    """création d'une nouvelle interface pour l'achat d'actions"""

    fen1 = Tk()
    fen1.title("Achat des actions")

    explication = Label(fen1, text = "Nombre d'actions souhaitées : ")

    actions = IntVar()

    champ = Entry(fen1, textvariable = actions)
    
    bouton = Button(fen1, text = 'Valider', command = fen1.destroy)

    # disposition de tous les widgets créés à l'aide de la méthode grid()
    explication.grid(row = 1, column = 1, padx = 10, pady = 10)
    champ.grid(row = 1, column = 2, padx = 10, pady = 10)
    bouton.grid(row = 1, column = 3, padx = 10, pady = 10)
        
    fen1.mainloop()
    

def confirmer_achat() :
    """fonction créant une petite interface graphique confirmant l'achat"""

    showinfo("Confirmation de l'achat",
             "Vous avez bien fait l'acquisition de vos actions")

def vendre() :
    """création d'une nouvelle interface pour la vente d'actions"""

    fen2 = Tk()
    fen2.title("Vente des actions")

    explication = Label(fen2, text = "Nombre d'actions à mettre sur le marché")

    actions = IntVar()

    champ = Entry(fen2, textvariable = actions)
    
    bouton = Button(fen2, text = 'Valider', command = fen2.destroy)

    # disposition de tous les widgets créés à l'aide de la méthode grid()
    explication.grid(row = 1, column = 1, padx = 10, pady = 10)
    champ.grid(row = 1, column = 2, padx = 10, pady = 10)
    bouton.grid(row = 1, column = 3, padx = 10, pady = 10)
    
    fen2.mainloop()

def confirmer_vente() :
    """affichage d'un message confirmant la vente"""

    showinfo("Confirmation de la vente",
             "Les actions ont bien été mises en vente")
    

def modifier_periode() :
    """affichage d'une fenêtre avec un curseur pour modifier la période"""

    fen3 = Tk()
    fen3.title("Modification de la période")

    # création d'un nouveau widget de type scale
    echelle = Scale(fen3, from_ = 1, to = 10, resolution = 1,
                    orient = HORIZONTAL, length = 250, tickinterval = 1,
                    showvalue = 0, label = 'Nouvelle période :',
                    command = maj_periode)
                    
    bouton = Button(fen3, text = 'Valider', command = fen3.destroy)
    echelle.grid(row = 1, padx = 10, pady = 10)
    bouton.grid(row = 2, padx = 10, pady = 10)

    fen3.mainloop()
  

def tracer_segments() :
    """fonction qui permet les tracés successifs de segments aléatoires"""

    global pt
    global T
    global arret
    global variance
    global esperance
    global independance

    # condition qui permet l'arrêt de l'exécution de la fonction 
    if arret :
        return None

    if not independance and len(fonctions.data) >= 2:
        variation_param_loi_norm()
        
    
    loi_norm = random.gauss(esperance, variance)

    
    x_1 = pt[0] + T*10
    y_1 = pt[1] + loi_norm*(-10)
    
    # utilisation de la méthode create_line() appliquée à l'objet canevas :
    canevas.create_line(pt[0], pt[1], x_1, y_1, width = 3, fill = 'red')
    
    pt = (x_1, y_1) # mise à jour du point d'arrivée d'où on repartira

    # envoi à la fonction permettant le stockage de toutes les valeurs
    fonctions.stocker(pt)


    # utilisation de la méthode after() appliquée à l'objet fenetre.
    # Elle permet d'exécuter une action après un temps donné en ms.
    if x_1 < 1000 :
        fenetre.after(T*1000, tracer_segments)


def tracer_axes(T) :
    """trace le repère en fonction de la période puis fait appel
    à la fonction tracer_segment"""

    # quadrillage :

    # axes horizontaux (en fonction de la période T)
    abscisse = 10
    while abscisse <= 985 :
        canevas.create_line(abscisse, 0, abscisse, 400, width = 1,
                            dash = (4, 4), fill = 'grey')
        abscisse = abscisse + T*10

    # axe verticaux
    ordonnee = 30
    while ordonnee <= 390 :
        canevas.create_line(0, ordonnee, 1000, ordonnee, width = 1,
                            dash = (4, 4), fill = 'grey')
        ordonnee = ordonnee + 20

    # affichage des axes :

    # axe des abscisses
    canevas.create_line(5, 390, 995, 390, width = 3,
                        fill = 'white', arrow = LAST)
    # axe des ordonnées
    canevas.create_line(10, 395, 10, 10, width = 3,
                        fill = 'white', arrow = LAST)  


def demarrer() :
    """fonction répondant à l'utilisateur lorsqu'il appuie sur le bouton
    démarrer. Permet le démarrage du tracé (des axes et de la courbe)."""

    global T
    global arret
    global pt

    # on définit les coordonnées de l'ordonnée à l'origine sous forme de tuple :
    pt = [10, 200]
    
    arret = False
    tracer_axes(T)
    fenetre.after(3000, tracer_segments)
    afficher_notifications()


def importer_texte() :
    """Cette fonction retourne au hasard une des phrases située
    dans un fichier texte"""

    global possibilites

    if possibilites == [] :
        with open('notifications.txt') as fichier :
            possibilites = fichier.readlines()
            choix = [i for i in range(len(possibilites))]
            indice = random.choice(choix)
            phrase = possibilites[indice]
            phrase = phrase[:-1] # permet d'éliminer les '\n'
            del possibilites[indice]
    else :
        choix = [i for i in range(len(possibilites))]
        indice = random.choice(choix)
        phrase = possibilites[indice]
        phrase = phrase[:-1]  # permet d'éliminer les '\n'
        del possibilites[indice]

    return phrase


def afficher_notifications() :
    """fonction permettant l'affichage d'une notification dans le fil
    d'actualité"""

    global y

    barre_notifs.create_text(5, y, text = importer_texte(), anchor = W)
    y = y + 20
    if y < 500 :
        barre_notifs.after(4000, afficher_notifications)

def variation_param_loi_norm():

    global variance
    global esperance

    point1 = fonctions.data[len(fonctions.data) - 1]
    point0 = fonctions.data[len(fonctions.data) - 2]

    if point1[1] < point0[1]:
        esperance = esperance - 0.5

    else:
        esperance = esperance + 0.5
    print(esperance)


def accueillir():

    global T
    global variance
    global esperance
    global independance
    independance = False
    
    accueil = Tk()
    accueil.title("Accueil")

    espace = 50

    canevas = Canvas(width = 100, height = 50, bg = 'orange')
    canevas.grid(row = 1, column = 1, columnspan = 2, padx = espace, pady = espace)

    text0 = Label(text='Période')
    text1 = IntVar()
    text1.set("2")
    entr1 = Entry(accueil, text = text1)


    text2 = Label(text='Variance')
    text3 = DoubleVar()
    text3.set("1")
    entr2 = Entry(accueil, text = text3)

    text4 = Label(text='Espérance')
    text5 = DoubleVar()
    text5.set("0")
    entr3 = Entry(accueil, text = text5)

    text0.grid(row = 2, column = 1, padx = espace, pady = espace)
    entr1.grid(row = 2, column = 2, padx = espace, pady = espace)
    text2.grid(row = 3, column = 1, padx = espace, pady = espace)
    entr2.grid(row = 3, column = 2, padx = espace, pady = espace)
    text4.grid(row = 4, column = 1, padx = espace, pady = espace)
    entr3.grid(row = 4, column = 2, padx = espace, pady = espace)

    valider = Button(accueil, text = 'valider', command = accueil.destroy)
    valider. grid(row = 5, column = 2, padx = espace, pady = espace)
    accueil.mainloop()

    T = text1.get()
    variance = text3.get()
    esperance = text5.get()

# ----- Procédure : -----

y = 10
possibilites = []
T = 2


accueillir()

fenetre = Tk()
fenetre.title("Logiciel de simulation des marchés financiers")

# initialisation de l'objet canevas à partir de la classe Canvas() :
titre1 = Canvas(fenetre, width = 1000, height = 50, bg = 'dark blue')
canevas = Canvas(fenetre, width = 1000, height = 400, bg = 'black')
titre2 = Canvas(fenetre, width = 300, height = 50, bg = 'blue')
barre_notifs = Canvas(fenetre, width=300, height=500, bg='White')

titre1.create_text(500, 25, text = 'Ecran de contrôle', fill = 'white')
titre2.create_text(150, 25, text = 'Flux d\'actualité', fill = 'white')

# affichage :
titre1.grid(row = 1, column = 1, columnspan = 4, padx = 10, pady = 10)
canevas.grid(row = 2, column = 1, columnspan = 4, padx = 10, pady = 10)
titre2.grid(row = 1, column = 5, padx = 10, pady = 10)
barre_notifs.grid(row = 2, column = 5, rowspan = 2, padx = 10, pady = 10)

# initialisation d'objets de classe Button() :
bouton1 = Button(fenetre, text = 'Démarrer', command = demarrer)
bouton2 = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
bouton3 = Button(fenetre, text = 'Acheter des actions', command = acheter)
bouton4 = Button(fenetre, text = 'Vendre des actions', command = vendre)
# affichage :
bouton1.grid(row = 3, column = 1, padx = 10, pady = 10)
bouton2.grid(row = 3, column = 2, padx = 10, pady = 10)
bouton3.grid(row = 3, column = 3, padx = 10, pady = 10)
bouton4.grid(row = 3, column = 4, padx = 10, pady = 10)

# Création d'un menu :
barre_menu = Menu(fenetre)

# Mise en place des différentes fonctionnalités de ce menu :
menufichier = Menu(barre_menu, tearoff = 0)
menufichier.add_command(label = 'Effacer tout', command = effacer)
menufichier.add_command(label = 'Quitter', command = fenetre.destroy)
barre_menu.add_cascade(label = 'Fichier', menu = menufichier)

menuoptions = Menu(barre_menu, tearoff = 0)
menuoptions.add_command(label = 'Modifier période', command = modifier_periode)
menuoptions.add_command(label = 'Personnaliser', command = personnaliser)
barre_menu.add_cascade(label = 'Options', menu = menuoptions)

menuaide = Menu(barre_menu, tearoff = 0)
menuaide.add_command(label = 'A propos', command = Apropos)
barre_menu.add_cascade(label = 'Aide', menu = menuaide)

# affichage :
fenetre.config(menu = barre_menu)

# démarrage du réceptionnaire d'évènements associé à la fen1être
fenetre.mainloop()

