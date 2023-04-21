# -*- coding: utf-8 -*-

# Oeuvrard Dilien TD - C
# Zaverio Lucas TD - C

from fltk import *
from random import *
from variable import *


sommet_bonus = [[1,0],[0,1],[-1,0],[0,-1]]

taille_case, taille_marge = 120,10


def evenement():
    
    """ 
    Cette fonction sert à créer les types d'évenements.
    """
    
    event = donne_ev()
    type = type_ev(event)
    mise_a_jour()
    return event, type

                ### ### ### ___ --- MENUS --- ___ ### ### ###

def jeu_graphique(largeur,hauteur):
    
    """
    Cette fonction à pour objetcif de créer la fenêtre graphique du jeu avec un fond blanc, en prenant en paramètre
    une largeur et une hauteur.
    """

    cree_fenetre(taille_case*largeur+taille_marge*2,taille_case*hauteur+taille_marge*2)
    rectangle(0,0,taille_case*largeur+taille_marge*largeur,taille_case*hauteur+taille_marge*hauteur,couleur='white', remplissage='white')


def open_menu():
    
    """
    Cette fonction ouvre la fenêtre de jeu avec un fond qui sera ici une image représentant le menu du jeu.
    
    >>> open_menu()
    True
    """
    
    cree_fenetre(700,700)
    image(350, 350, "images/background.png", ancrage = "center") 
    return True
    

def open_param():
    
    """ 
    Cette fonction permet l'affichage graphique du menu paramètre, une image où toutes les difficultés de jeu
    sont présentes.
    
    >>> open_param()
    True
    """
    
    image(350, 350, "images/back_param.png", ancrage = "center") 
    return True


def open_info():
    
    """ 
    Cette fonction permet l'affichage graphique du menu information, une image où il est expliqué ce qu'est le 
    slitherlink et comment y jouer.
    
    >>> open_info()
    True
    """
    
    image(350, 350, "images/back_info.png", ancrage = "center") 
    return True


def clic_menu(event):
    
    """
    Cette fonction permet de créer les zones qui seront cliquables dans la fenêtre graphique du menu,
    une zone sur le rectangle "jouer" et une autre sur "l'engrenage".
    Le rectangle "jouer" et "l'engrenage" étant intégrés dans la fenêtre graphique du menu du jeu.
    >>> clic_menu(event)
    True, False, True, False, True
    """
    
    # Bouton pour jouer
    if 211 <= abscisse(event) <= 478 and 432 <= ordonnee(event) <= 507:
        return True, False, True, False, True
        
    # Bouton paramètres    
    elif 653 <= abscisse(event) <= 692 and 5 <= ordonnee(event) <= 44:
        return True, False, False, True, False
    
    else:
        return True, True, False, False, False
    

def interaction_menu(type, event):
    
    """
    Cette fonction permet à partir de la fenêtre graphique du menu du jeu de soit fermer le jeu en faisant un clique gauche
    de la souris sur la croix en haut à droite de la fenêtre graphique du menu, soit de se rendre soit sur la fenêtre graphique
    "paramètre" en faisant un clique gauche de la souris sur le rectangle "jouer" se trouvant au mileu de la
    fenêtre graphique du menu, ou soit de se rendre sur la fenêtre graphique "information" en faisant un clique gauche de la 
    souris sur l'engrenage en haut à droite de la fenêtre graphique du menu.
    """
    
    if type == 'Quitte':
                
        return False, False, False, False, False
            
    elif type == 'ClicGauche':
        
        return clic_menu(event)
            
    else:
        return True, True, False, False, False
                
    
    

def clic_info(event):
    
    """ 
    Cette fonction permet de créer la zone cliquable "retour" sur la "flèche" en haut à gauche de la
    fenêtre graphique "information".
    Cette flèche étant intégrer dans la fenêtre graphique "information".
    """
    
    # Bouton Retour
    if 7 <= abscisse(event) <= 48 and 6 <= ordonnee(event) <= 50:
        return True, True, False, False
    else:
        return True, False, False, True
    
def interaction_info(type,event):
    
    """
    Cette fonction permet à partir de la fenêtre graphique "information" du jeu de, soit fermer le jeu en faisant
    un clique gauche de la souris sur la croix en haut à droite de la fenêtre graphique "information", où 
    soit de revenir en arrière c'est à dire de revenir sur la fenêtre graphique du menu en faisant un clique gauche
    sur la "flèche" en haut à gauche de la fenêtre graphique "information".
    """
    
    if type == 'Quitte':     
        return False, False, False, False
            
    elif type == 'ClicGauche':  
        return clic_info(event)
            
    else:
        return True, False, False, True
            
def clic_param(event):
    
    """ 
    Cette fonction permet de créer les zones qui seront cliquables dans la fenêtre graphique "paramètre",
    une zone sur chaque rectangles "Trivial","Facile","Moyen" et "Diffcile" et une autre sur "le flèche".
    Les rectangles "Trivial","Facile","Moyen" et "Diffcile" et "le flèche" étant intégrés dans la fenêtre 
    graphique du menu paramètre.
    """
    
    # Bouton Retour
    if 7 <= abscisse(event) <= 48 and 6 <= ordonnee(event) <= 50:
        return True, True, False, False, None
        
    # TRIVIAL
    elif 63 <= abscisse(event) <= 330 and 285 <= ordonnee(event) <= 360:
        return True, False, False, True, "grilles/grille-triviale.txt"
        
    # FACILE
    elif 370 <= abscisse(event) <= 637 and 285 <= ordonnee(event) <= 360:
       return True, False, False, True, choice(Facile)
        
    # MOYEN
    elif 63 <= abscisse(event) <= 330 and 458 <= ordonnee(event) <= 533:
        return True, False, False, True, choice(Moyen)
    
    # DIFFICILE
    elif 370 <= abscisse(event) <= 637 and 458 <= ordonnee(event) <= 533:
        return True, False, False, True, choice(Difficile)
    
    else: 
        return True, False, True, False, None
    
    
def interaction_param(type,event):
    
    """ 
    Cette fonction permet à partir de la fenêtre graphique "paramètre" du jeu de, soit fermer le jeu en faisant
    un clique gauche de la souris sur la croix en haut à droite de la fenêtre graphique "paramètre", 
    soit de revenir en arrière c'est à dire de revenir sur la fenêtre graphique du menu en faisant un clique gauche
    sur la "flèche" en haut à gauche de la fenêtre graphique "paramètre" ou soit de faire un clique gauche sur l'une des quatres
    difficultés pour lancé le jeu danc la difficulté choisie.
    
    """
    
    if type == 'Quitte':
        return False, False, False, False, None
    
    elif type == 'ClicGauche':
        
        return clic_param(event)
    
    else:
        return True, False, True, False, None
                
    
def recherche_segment(event,largeur,hauteur):
    
    """
    Cette fonction recherche les segments par rapport à la position du clic
    """

    trait_x = fct_abc(abscisse(event),largeur,hauteur)
    trait_y = fct_abc(ordonnee(event),largeur,hauteur)

    return cherche_segment(abscisse(event),ordonnee(event)), trait_x,trait_y
                    



                ### ### ### ___ --- FONCTIONS IMPORTANTS --- ___ ### ### ###
def angle(largeur,hauteur):
    
    """ 
    Cette fonction sert à créer les points (angles).
    >>> angle(largeur,hauteur)
    None
    """

    for i in range(largeur+1):
        for j in range(hauteur+1):
            point(taille_marge + i * taille_case, taille_marge + j * taille_case,epaisseur = 2)
            

def indice(grille):

    temp_1 = -taille_case
    for i in grille:
        temp_1 += taille_case
        temp_2 = -taille_case
        for cont in i:
            temp_2 += taille_case
            if cont != None:
                y,x = temp_1+taille_case/2, temp_2+taille_case/2
                texte(x,y,cont)


def clic_x(largeur,hauteur, x):
    
    """ 
    Cette fonction gère les clics effectués sur les position abscisses 
    """

    for i in range(largeur+1):
        for j in range(hauteur+1):
            if - 5 < x - (taille_marge + i * taille_case) < 5:
                return True
    return False


def clic_y(largeur,hauteur, y):
    
    """
    Cette fonction gère les clics effectués sur les position ordonnés
    """

    for i in range(largeur+1):
        for j in range(hauteur+1):
            if - 5 < y - (taille_marge + j * taille_case) < 5:
                return True
    return False


def fct_abc(x,a,b):
    
    return clic_x(a,b, x)


def fct_ord(y,a,b,taille_case, taille_marge):
    
    return clic_y(a,b, y)
    

def carte_creation(carte):
    
    """
    Fonction renvoyant la liste grille grace à l'ouverture du fichier 
    au préalable
    """
    
    fichier = open(carte, "r")
    carte = fichier.readlines()
    fichier.close()
    grille = grille_creation(carte)    
    return grille
    

def grille_creation(carte, grille = []):
    
    """ 
    Fonction renvoyant une liste grille dans laquelle on retrouve
    les coordonnées des case d'un ficher
    """
    
    liste_allow = ["_", "\n", "1","0", "2", "3"]
    
    for ligne in range(len(carte)):
        temp = []
        for case in range(len(carte[ligne])):
            if not carte[ligne][case] in liste_allow:
                return False
            if carte[ligne][case] == "_":
                temp.append(None)    
            elif carte[ligne][case] != "\n":
                temp.append(int(carte[ligne][case]))
        grille.append(temp)
    return grille


def interface_graphique(largeur,hauteur,grille):
    
    """ 
    Cette fonction sert à créer l'interface graphique du jeu
    """
    
    jeu_graphique(len(grille[0]),len(grille))
    angle(len(grille[0]),len(grille))
    indice(grille)
    return cotes_dico(grille)

                ### ### ### ___ --- INTERFACE GRAPHIQUE --- ___ ### ### ###
                
def tracage(etat, segment,sauvegarde,liste_sauvegarde):
    
    """ 
    Cette fonction permet de tracé les segments entre chaques points.
    """
    if est_interdit(etat, segment) == False and not sauvegarde:
        
        if est_trace(etat, segment):
            effacer_segment(etat, segment)
            ligne(segment[0][0]*taille_case+taille_marge,
                  segment[0][1]*taille_case+taille_marge,
                  segment[1][0]*taille_case+taille_marge,
                  segment[1][1]*taille_case+taille_marge, 
                  couleur="white")
            return "blank",liste_sauvegarde
        else:
            tracer_segment(etat, segment)
            ligne(segment[0][0]*taille_case+taille_marge,
                  segment[0][1]*taille_case+taille_marge,
                  segment[1][0]*taille_case+taille_marge,
                  segment[1][1]*taille_case+taille_marge)
            return "plein",liste_sauvegarde
    elif est_interdit(etat, segment) == False and sauvegarde:
        if est_trace(etat, segment):
            effacer_segment(etat, segment)
            ligne(segment[0][0]*taille_case+taille_marge,
                  segment[0][1]*taille_case+taille_marge,
                  segment[1][0]*taille_case+taille_marge,
                  segment[1][1]*taille_case+taille_marge, 
                  couleur="white")
            liste_sauvegarde.remove(segment)
            return "blank",liste_sauvegarde
        else:
            tracer_segment(etat, segment)
            ligne(segment[0][0]*taille_case+taille_marge,
                  segment[0][1]*taille_case+taille_marge,
                  segment[1][0]*taille_case+taille_marge,
                  segment[1][1]*taille_case+taille_marge,
                  couleur="blue")
            liste_sauvegarde.append(segment)
            return "plein",liste_sauvegarde
    else:
        return "croix",liste_sauvegarde
    
    
def mode_sauvegarde(sauvegarde, liste_sauvegarde, etat):
    
    """
    Cette fonction de sauvegarder les segments trcés si le mode sauvegarde est actif,
    puis de les effacer si cette fonction est désactivée.
    """
    
    if sauvegarde:
        print("Mode sauvegarde Inactif")
        sauvegarde = False
        for i in range(len(liste_sauvegarde)):
            effacer_segment(etat, liste_sauvegarde[i])
            ligne(liste_sauvegarde[i][0][0]*taille_case+taille_marge,
                  liste_sauvegarde[i][0][1]*taille_case+taille_marge,
                  liste_sauvegarde[i][1][0]*taille_case+taille_marge,
                  liste_sauvegarde[i][1][1]*taille_case+taille_marge, 
                  couleur="white")
    
    else:   
        print("Mode sauvegarde Actif")
        sauvegarde = True
        liste_sauvegarde = []
    return sauvegarde,liste_sauvegarde
     

def croix(etat, segment):
    
    """ 
    Cette fonction sert à créer les croix pour indiquer un segment n'est pas
    tracable.
    """

    if not est_trace(etat,segment):
        if est_interdit(etat, segment):
            effacer_segment(etat, segment)
            if segment[0][0] == segment[1][0]:
                vertical_supcroix(segment)
            else:   horizontal_supcroix(segment)
        else:
            interdire_segment(etat, segment)
            if segment[0][0] == segment[1][0]:
                vertical_croix(segment)
            else: horizontal_croix(segment)


def vertical_croix(segment):
    
    """ 
    Créaction croix verticale.
    """

    ligne(segment[0][0]*taille_case,
            segment[0][1]*taille_case+taille_case/2,
            segment[1][0]*taille_case+taille_marge*2,
            segment[1][1]*taille_case-taille_case/3,
            couleur="red", epaisseur="2")

    ligne(segment[0][0]*taille_case+taille_marge*2,
            segment[0][1]*taille_case+taille_case/2,
            segment[1][0]*taille_case,
            segment[1][1]*taille_case-taille_case/3,
            couleur="red", epaisseur="2")


def horizontal_croix(segment):

    """ 
    Créaction croix horizontale.
    """

    ligne(segment[0][0]*taille_case+taille_case/2,
            segment[0][1]*taille_case,
            segment[1][0]*taille_case-taille_case/3,
            segment[1][1]*taille_case+taille_marge*2,
            couleur="red", epaisseur="2")

    ligne(segment[0][0]*taille_case+taille_case/2,
            segment[0][1]*taille_case+taille_marge*2,
            segment[1][0]*taille_case-taille_case/3,
            segment[1][1]*taille_case,
            couleur="red", epaisseur="2")


def vertical_supcroix(segment):

    """
    suppression croix verticale.
    """

    ligne(segment[0][0]*taille_case,
            segment[0][1]*taille_case+taille_case/2,
            segment[1][0]*taille_case+taille_marge*2,
            segment[1][1]*taille_case-taille_case/3,
            couleur="white", epaisseur="2")

    ligne(segment[0][0]*taille_case+taille_marge*2,
            segment[0][1]*taille_case+taille_case/2,
            segment[1][0]*taille_case,
            segment[1][1]*taille_case-taille_case/3,
            couleur="white", epaisseur="2")


def horizontal_supcroix(segment):

    """
    suppression croix horizontale.
    """

    ligne(segment[0][0]*taille_case+taille_case/2,
            segment[0][1]*taille_case,
            segment[1][0]*taille_case-taille_case/3,
            segment[1][1]*taille_case+taille_marge*2,
            couleur="white", epaisseur="2")

    ligne(segment[0][0]*taille_case+taille_case/2,
            segment[0][1]*taille_case+taille_marge*2,
            segment[1][0]*taille_case-taille_case/3,
            segment[1][1]*taille_case,
            couleur="white", epaisseur="2")
    

def cotes_dico(indices):
    
    """
    Fonction renvoyant un dictionnaire avec l'entièreté des relations entre cotés.
    """
    
    etat = {}
    for i in range(len(indices)+1):
        for j in range(len(indices[0])):
            etat[(j,i),(j+1,i)] = 0
    for h in range(len(indices)):
        for k in range(len(indices[0])+1):
            etat[(k,h),(k,h+1)] = 0
    return etat

                ### ### ### ___ --- FONCTIONS SEGMENTS --- ___ ### ### ###

def est_trace(etat, segment):
    
    """ 
    Fonction renvoyant True si segment est tracé dans etat, et False sinon 
    """
    
    if (segment in etat):
        if etat[segment] == 1:
            return True
        else: return False


def est_interdit(etat, segment): 
    
    """ 
    Fonction renvoyant True si segment est interdit dans etat, et False sinon
    >>>est_interdit(etat, ((0,1),(1,1)))
    True
    """
    if (segment in etat):
        if etat[segment] == -1:
            return True
        else: return False
    

def est_vierge(etat, segment) : 
    
    """ 
    Fonction renvoyant True si segment est vierge dans etat, et False sinon 
    >>> est_vierge(etat, ((0,1),(1,1)))
    None
    """
    
    if (segment not in etat):
        return True
    

def tracer_segment(etat, segment):
    
    """
    Fonction modifiant etat afin de représenter le fait que segment est maintenant tracé 
    """
    
    etat[segment] = 1
    return etat


def cherche_segment(x,y):

    bord = [taille_marge,
            taille_case+taille_marge,
            taille_case*2+taille_marge,
            taille_case*3+taille_marge,
            taille_case*4+taille_marge,
            taille_case*5+taille_marge,
            taille_case*6+taille_marge,
            taille_case*7+taille_marge,
            taille_case*8+taille_marge]

    for i in bord:
        if i-5 < x < i+5:
            return ((x//120,y//120),((x//120),(y//120)+1))
    return ((x//120,y//120),((x//120)+1,y//120))
    
    

def interdire_segment(etat, segment):
    
    """
    Fonction  modifiant etat afin de représenter le fait que segment est maintenant interdit 
    """
    
    etat[segment] = -1
    return etat



def effacer_segment(etat, segment): 
    
    """ 
    Fonction modifiant etat afin de représenter le fait que segment est maintenant vierge. 
    Attention, effacer un segment revient à retirer de l’information du dictionnaire etat
    """
    
    etat[segment] = 0
    return etat


def segments_traces(etat, sommet) : 
    
    """
    Fonction renvoyant la liste des segments tracés adjacents à sommet dans etat
    """  
    
    liste_trace=[]
    if ((sommet[0]-1,sommet[1]) in etat):
        if (etat[sommet[0]-1,sommet[1]]) == 1:
            liste_trace.append((sommet[0]-1,sommet[1]))
    if ((sommet[0]+1,sommet[1]) in etat):
        if (etat[sommet[0]+1,sommet[1]]) == 1:
            liste_trace.append((sommet[0]+1,sommet[1]))
    if ((sommet[0],sommet[1]-1) in etat):
        if (etat[sommet[0],sommet[1]-1]) == 1:
            liste_trace.append((sommet[0],sommet[1]-1))
    if ((sommet[0],sommet[1]+1) in etat):
        if (etat[sommet[0],sommet[1]+1]) == 1:
            liste_trace.append((sommet[0]-1,sommet[1]+1))
    return liste_trace


def segments_interdits(etat, sommet) : 
    
    """ 
    Fonction renvoyant la liste des segments interdits adjacents sommet dans etat
    """
    
    liste_interdit=[]
    if ((sommet[0]-1,sommet[1]) in etat):
        if (etat[sommet[0]-1,sommet[1]]) == -1:
            liste_interdit.append((sommet[0]-1,sommet[1]))
    if ((sommet[0]+1,sommet[1]) in etat):
        if (etat[sommet[0]+1,sommet[1]]) == -1:
            liste_interdit.append((sommet[0]+1,sommet[1]))
    if ((sommet[0],sommet[1]-1) in etat):
        if (etat[sommet[0],sommet[1]-1]) == -1:
            liste_interdit.append((sommet[0],sommet[1]-1))
    if ((sommet[0],sommet[1]+1) in etat):
        if (etat[sommet[0],sommet[1]+1]) == -1:
            liste_interdit.append((sommet[0]-1,sommet[1]+1))
    return liste_interdit


def segments_vierges(etat, sommet,liste_vierge=[]): 
    
    """
    Fonction renvoyant la liste des segments vierges adjacents à sommet dans etat 
    """
    
    if ((sommet[0]-1,sommet[1]) not in etat):
        liste_vierge.append((sommet[0]-1,sommet[1]))
    if ((sommet[0]+1,sommet[1]) not in etat):
        liste_vierge.append((sommet[0]+1,sommet[1]))
    if ((sommet[0],sommet[1]-1) not in etat):
        liste_vierge.append((sommet[0],sommet[1]-1))
    if ((sommet[0],sommet[1]+1) not in etat):
        liste_vierge.append((sommet[0]-1,sommet[1]+1))
    return liste_vierge

        



                ### ### ### ___ --- FONCTIONS VICTOIRE --- ___ ### ### ###
                
def verification(verif_indices):

    """ 
    Cette fonction permet de gérer la victoire en vérifiant si les indices
    sont remplis
    """
    
    for i in verif_indices:
        if i == -1 or i == 1:
            return False
    return True


def statuts_verif(indices, etat):
    
    """ 
    Fonction suppléante de la précédente.
    """
    
    verif_list=[]
    for i in range(len(indices)):
        for j in range(len(indices[i])):
            a = (statut_case(indices, etat, [i,j]))
            verif_list.append(a)
            
    return verification(verif_list)


def statut_case(indices, etat, case):
    """ 
    
    Fonction recevant le tableau d’indices, l’état de la grille et les
    coordonnées d’une case (pas d’un sommet !) et renvoyant None si cette case ne porte aucun indice, et un nombre entier sinon :
        – 0 si l’indice est satisfait ;
        – positif s’il est encore possible de satisfaire l’indice en traçant des segments autour de la case ;
        – négatif s’il n’est plus possible de satisfaire l’indice parce que trop de segments sont déjà tracés ou interdits autour de la case.
    
    """
    
    trace,interdit = 0,0
    if indices[case[0]][case[1]] == None:
        return None
    if ((case[1],case[0]),(case[1]+1,case[0]) in etat):
        if est_trace(etat, ((case[1],case[0]),(case[1],case[0]+1))):
            trace += 1
        else: interdit += 1
        if est_trace(etat, ((case[1],case[0]),(case[1]+1,case[0]))):
            trace += 1
        else: interdit += 1
        if est_trace(etat, ((case[1]+1,case[0]),(case[1]+1,case[0]+1))):
            trace += 1
        else: interdit += 1
        if est_trace(etat, ((case[1],case[0]+1),(case[1]+1,case[0]+1))):
            trace += 1
        else: interdit += 1
        if trace == indices[case[0]][case[1]]:
            return 0
        elif trace < indices[case[0]][case[1]] or trace + interdit < indices[case[0]][case[1]]:
            return 1
        elif trace > indices[case[0]][case[1]] or interdit - trace >= indices[case[0]][case[1]]:
            return -1
                
def longueur_boucle(etat, segment, depart, precedent, courant,seg_parcours,_trait_,liste_segments):
    
    """ 
    Fonction qui sert à dire si une fonction est bien bouclé ou non.
    """

    seg_parcours += 1
    if _trait_ == "blank":
        if liste_segments:
            courant = liste_segments[-1]
            liste_segments.pop()
    indice = verif_seg_depart(etat,depart)

    if courant != depart:
        indice_2 = verif_seg_courant(etat,courant)
        if indice_2 != 2:
            return [False,precedent,courant,seg_parcours]
        else:
            liste_segments.append(precedent)
            precedent = courant
            courant_temp = seg_courant_adja(etat,courant,precedent)
            courant = courant_temp[1]
        if indice != 2: 
            return [False,precedent,courant,seg_parcours,liste_segments]
    return [True,precedent,courant,seg_parcours,liste_segments]
    
    if indice != 2: 
        return [False,precedent,courant,seg_parcours]

def seg_courant_adja(etat,courant,precedent):
    
    """
    Fonction qui recherche les segments adjacents.
    """
    
    if ((courant,(courant[0]+1,courant[1])) in etat):
        if (etat[(courant,(courant[0]+1,courant[1]))] == 1  
            and (courant,(courant[0]+1,courant[1])) != precedent):
            return (courant,(courant[0]+1,courant[1]))
    
    if (((courant[0]+1,courant[1]),courant) in etat):
        if (etat[((courant[0]+1,courant[1]),courant)] == 1
            and ((courant[0]+1,courant[1]),courant) != precedent):
            return ((courant[0]+1,courant[1]),courant)
            
            
    if ((courant,(courant[0],courant[1]+1)) in etat):
        if (etat[(courant,(courant[0],courant[1]+1))] == 1 
            and (courant,(courant[0],courant[1]+1)) != precedent):
            return (courant,(courant[0],courant[1]+1))
    
    if (((courant[0],courant[1]+1),courant) in etat):
        if (etat[((courant[0],courant[1]+1),courant)] == 1
            and ((courant[0],courant[1]+1),courant) != precedent):
            return ((courant[0],courant[1]+1),courant)
            
            
    if ((courant,(courant[0]-1,courant[1])) in etat):
        if (etat[(courant,(courant[0]-1,courant[1]))] == 1  
            and (courant,(courant[0]-1,courant[1])) != precedent):
            return (courant,(courant[0]-1,courant[1]))
    
    if (((courant[0]-1,courant[1]),courant) in etat):
        if (etat[((courant[0]-1,courant[1]),courant)] == 1
            and ((courant[0]-1,courant[1]),courant) != precedent):
            return ((courant[0]-1,courant[1]),courant)
            
            
    if ((courant,(courant[0],courant[1]-1)) in etat):
        if (etat[(courant,(courant[0],courant[1]-1))] == 1  
            and (courant,(courant[0],courant[1]-1)) != precedent):
            return (courant,(courant[0],courant[1]-1))
    
    if (((courant[0],courant[1]-1),courant) in etat):
        if (etat[(courant,(courant[0],courant[1]-1),courant)] == 1
            and ((courant[0],courant[1]-1),courant) != precedent):
            return ((courant[0],courant[1]-1),courant)

def verif_seg_courant(etat,courant,indice=0):
    
    """ 
    Fonction qui recherche les segments adjacents à partir d'un sommet
    """
             
    if ((courant,(courant[0]+1,courant[1])) in etat):
        if etat[(courant,(courant[0]+1,courant[1]))] == 1:  
            indice += 1
    
    if (((courant[0]+1,courant[1]),courant) in etat):
        if etat[((courant[0]+1,courant[1]),courant)] == 1:
            indice += 1
            
            
    if ((courant,(courant[0],courant[1]+1)) in etat):
        if etat[(courant,(courant[0],courant[1]+1))] == 1:  
            indice += 1
    
    if (((courant[0],courant[1]+1),courant) in etat):
        if etat[((courant[0],courant[1]+1),courant)] == 1:
            indice += 1
            
            
    if ((courant,(courant[0]-1,courant[1])) in etat):
        if etat[(courant,(courant[0]-1,courant[1]))] == 1:  
            indice += 1
    
    if (((courant[0]-1,courant[1]),courant) in etat):
        if etat[((courant[0]-1,courant[1]),courant)] == 1:
            indice += 1
            
            
    if ((courant,(courant[0],courant[1]-1)) in etat):
        if etat[(courant,(courant[0],courant[1]-1))] == 1:  
            indice += 1
    
    if (((courant[0],courant[1]-1),courant) in etat):
        if etat[((courant[0],courant[1]-1),courant)] == 1:
            indice += 1
            
    return indice


def verif_seg_depart(etat,depart,indice=0):
    
    """
    Vérifie combien de segments sont dessinné à côté du sommet de départ.
    """
    
    
    if ((depart,(depart[0]+1,depart[1])) in etat):
        if etat[(depart,(depart[0]+1,depart[1]))] == 1:
            indice += 1
    if ((depart,(depart[0],depart[1]+1)) in etat):
        if etat[(depart,(depart[0],depart[1]+1))] == 1:
            indice += 1 
    if ((depart,(depart[0]-1,depart[1])) in etat):
        if etat[(depart,(depart[0]-1,depart[1]))] == 1:
            indice += 1
    if ((depart,(depart[0],depart[1]-1)) in etat):
        if etat[(depart,(depart[0],depart[1]-1))] == 1:
            indice += 1
    if (((depart[0]+1,depart[1]),depart) in etat):
        if etat[((depart[0]+1,depart[1]),depart)] == 1:
            indice += 1
    if (((depart[0],depart[1]+1),depart) in etat):
        if etat[((depart[0],depart[1]+1),depart)] == 1:
            indice += 1 
    if (((depart[0]-1,depart[1]),depart) in etat):
        if etat[((depart[0]-1,depart[1]),depart)] == 1:
            indice += 1
    if (((depart[0],depart[1]-1),depart) in etat):
        if etat[((depart[0],depart[1]-1),depart)] == 1:
            indice += 1
    return indice
                
                
def victoire(param1,param2,largeur,hauteur):
    
    """ 
    Cette fonction permet d'afficher le message "Vous avez gagné" si les paramètres 1 et 2 sont "True",
    c'est à dire si les conditions,"chaque indice est satisfait" et "l'ensemble des segments tracés forme une unique
    boucle fermée".
    """
    
    if param1 == True and param2 == True:
        texte(10,taille_case*(hauteur/4)+taille_marge,"Vous avez gagné !",couleur="red")
        print("Vous avez gagné !")

                ### ### ### ___ --- FONCTIONS IA --- ___ ### ### ###

def bot_resolve(sommet, etat, indices,x,y):
    """
    Première fonction pour le solveur, ne fonctionne pas à 100% mais répond
    exactement à ce que la consigne nous demande de faire.
    """
    
    
    som_seg = bot_seg_adja(sommet,etat)
    
    if som_seg == 2:
        """La boucle est bouclée."""
        if bot_statuts_verif(indices, etat) == [0]*x*y:
            return True
        else: return False
        
    if som_seg > 2:
        return False
    
    if som_seg < 2:
        for i in sommet_bonus:
            new_sommet = (sommet[0] + i[0], sommet[1] + i[1])
            new_segment = (sommet,new_sommet)
            
        if new_segment in etat:
            etat = tracer_segment(etat, new_segment)
            
            if -1 in bot_statuts_verif(indices, etat):
                etat = effacer_segment(etat, new_segment)
                return False
            
            etat_solveur = bot_resolve(new_sommet, etat, indices,x,y)
            
            if etat_solveur:
                return True
            
            elif etat_solveur == False:
                etat = effacer_segment(etat, new_segment)
    return False


def bot_resolve2(sommet, etat, indices):
    
    """
    Seconde fonction pour le solveur. Problème avec de récursivité (error)
    """
    
    if bot_seg_adja(sommet,etat) == 2:
         """La boucle est bouclée."""
         if statuts_verif(grille, etat):
             print("Trouvé")
             return True
    elif bot_seg_adja(sommet,etat) > 2:
        return False
    elif bot_seg_adja(sommet,etat) < 2:
         temp_liste = [[1,0],[-1,0],[0,1],[0,-1]]
         # Boucle for pour faire,  les 4 côtés
         for i in range(len(temp_liste)):
             seg_rajoute = (sommet[0]+temp_liste[i][0],sommet[1]+temp_liste[i][1])
             segment_bot = ((sommet),(seg_rajoute))
             if segment_bot not in etat:
                 segment_bot = ((seg_rajoute),(sommet))
             if segment_bot in etat:
                 etat = tracer_segment(etat, segment_bot)
                 validation = bot_statuts_verif(indices, etat)
                 if -1 in validation:
                     etat = effacer_segment(etat, segment_bot)
                 etat_solveur = bot_resolve2(seg_rajoute, etat, indices)
                 if etat_solveur:
                     return True
                 elif etat_solveur == False:
                     etat = effacer_segment(etat, segment_bot)
         return False
    
    
def bot_statuts_verif(indices, etat):
    """
    Fonction pour vérifier le statut des indices.
    """
    
    bot_verif_list=[]
    for i in range(len(indices)):
        for j in range(len(indices[i])):
            a = (statut_case(indices, etat, [i,j]))
            bot_verif_list.append(a)
    return bot_verif_list
    
    
def bot_seg_adja(sommet, etat, indice = 0):
    
    """
    compte le nb de seg adj, pour le solveur.
    """
     
    if ((sommet, (sommet[0]+1,sommet[1])) in etat):
        if etat[sommet,(sommet[0]+1,sommet[1])] == 1:
            indice += 1
            
    if ((sommet, (sommet[0],sommet[1]+1)) in etat):
        if etat[sommet,(sommet[0],sommet[1]+1)] == 1:
            indice += 1
            
    if ((sommet, (sommet[0]-1,sommet[1])) in etat):
        if etat[sommet,(sommet[0]-1,sommet[1])] == 1:
            indice += 1
            
    if ((sommet,(sommet[0],sommet[1]-1)) in etat):
        if etat[sommet,(sommet[0],sommet[1]-1)] == 1:
            indice += 1
            
    if (((sommet[0]+1,sommet[1]), sommet) in etat):
        if etat[(sommet[0]+1,sommet[1]), sommet] == 1:
            indice += 1
            
    if (((sommet[0],sommet[1]+1), sommet) in etat):
        if etat[(sommet[0],sommet[1]+1), sommet] == 1:
            indice += 1
            
    if (((sommet[0]-1,sommet[1]), sommet) in etat):
        if etat[(sommet[0]-1,sommet[1]), sommet] == 1:
            indice += 1
            
    if (((sommet[0],sommet[1]-1), sommet) in etat):
        if etat[(sommet[0],sommet[1]-1), sommet] == 1:
            indice += 1
            
    return indice
