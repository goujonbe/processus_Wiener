def stocker(donnee) :
    """L'objectif de cette fonction est de stocker sous forme de liste
    toutes les valeurs prises par la courbe. (ce n'est pas exactement toutes
    les valeurs mais seulement les points de changement de courbure)."""

    # data stocke toutes les données qui sont envoyées à la fonction
    # il s'agit d'une liste de tuples
    global data

    data.append(donnee)
    return data



data = [(10, 200)]


