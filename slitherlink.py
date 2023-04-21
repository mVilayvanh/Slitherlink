# -*- coding: utf-8 -*-

# Oeuvrard Dilien TD - C
# Zaverio Lucas TD - C

from fltk import *
from random import *

from variable import *
from function import *

# BOUCLE DE JEU
while game: 
    
    # MENU DE JEU
    if __name__  == "__main__":
        jouer = False
        menu = open_menu()
        while menu:
            event, type = evenement()
            game, menu, jouer, info, parametre  = interaction_menu(type,event)
                    

    # MENU INFORMATION / PARAMETRE
    if info:
        information = open_info()
        while information:
            event, type = evenement()
            game, menu, jouer, information  = interaction_info(type,event)
            

    # L'AVANT PARTIE
    if parametre:
        param = open_param()
        while param:
            event, type = evenement()
            game,  menu , param, jouer, carte  = interaction_param(type,event)
                

    # LA PARTIE    
    if jouer:
        ferme_fenetre()
        seg_depart = 0
        grille = carte_creation(carte)
        
        if grille == False:
            print("Error, Format de grille non valide !")
            break
            
        else: 
            largeur, hauteur = len(grille[0]), len(grille)
            etat = interface_graphique(largeur, hauteur,grille)
        
        
        
        while True and grille != False:
            event, type = evenement()
            
            if type == 'Quitte':
                jouer, game = False, False                                
                break
            
            if type == "ClicGauche":
                segment,trait_x,trait_y = recherche_segment(event,largeur, hauteur)
                if trait_x == True or trait_y == True:
                    if seg_depart == 0:
                        
                        ## Déclaration de variables utilisées pour le fonctionnement du programme
                        seg_depart = 1
                        depart = segment[0]
                        precedent = segment[0]
                        courant = segment[1] 
                        seg_parcours = 0 
                            
                    # Tracage des traits.
                    _trait_, liste_sauvegarde = tracage(etat, segment, sauvegarde, liste_sauvegarde)
                    
                    # Paramètre de victoire (vérification indices satisfaits.)
                    param_win_1 = (statuts_verif(grille, etat))
                    
                    # Second paramètre de victoire.
                    longueur = longueur_boucle(etat, segment, depart, precedent, courant, seg_parcours, _trait_,liste_segments)
                    
                    #Transformation de la liste en plusieurs variables.
                    param_win_2 = longueur[0]
                    precedent = longueur[1]
                    courant = longueur[2]
                    seg_parcours = longueur[3]
                    
                    # Appel fonction, affichant victoire selon les paramètres.
                    victoire(param_win_1,param_win_2,largeur, hauteur)
                                                                           
            # Pour préciser qu'une ligne ne doit pas être tracé
            elif type == "ClicDroit":
                segment,trait_x,trait_y = recherche_segment(event,largeur, hauteur)
                if trait_x == True or trait_y == True:
                    croix(etat,segment)
    
            elif type == "Touche":
                
                # CODE TRICHE PAS 100 % FONCTIONNEL
                if touche(event) == "e" or touche(event) == "E":
                    print("Code Triche")
                    etat = bot_resolve(sommet, etat, grille,largeur, hauteur)
                    
                # / FONCTIONNALITE BROUILLON /
                elif touche(event) == "s" or touche(event) == "S":
                    sauvegarde, liste_sauvegarde = mode_sauvegarde(sauvegarde, liste_sauvegarde, etat)
                    
                    
    ferme_fenetre()