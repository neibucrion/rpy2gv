from graphviz import Digraph

#Creation du graphe final
graphe = Digraph(format = "png")
styleNoeuds = {'fontname':'Arial', 'shape':'ellipse', 'color': '#000000', 'style': 'filled', 'fillcolor':'#ffffff'}
graphe.node_attr.update(styleNoeuds)

#Ouverture du fichier de script
script = open("script.rpy","r")
lignes = script.readlines()
labelActuel = ""

#Boucle principale
for ligne in lignes:
    #Si label, le mémorise
    if 'label' in ligne:
        finligne = ligne.find(":")
        labelActuel = ligne[6:finligne]
        labelActuel = labelActuel.strip()
    #Si jump crée une nouvelle flèche dans le graphe
    elif 'jump' in ligne:
        finJump = ligne.find('jump')+4
        nomJump = ligne[finJump:]
        nomJump = nomJump.strip()
        graphe.edge(labelActuel,nomJump)

#Publie le graphe à la fois en code GV et en image PNG
graphe.render(filename="graphe")

#Et voilà le travail !