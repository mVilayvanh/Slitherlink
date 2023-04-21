# Oeuvrard Dilien TD - C
# Zaverio Lucas TD - C

# VARIABLES PRINCIPALES
game, parametre, jouer, info = True, False, False, False

Facile = ["grilles/grille-facile1.txt","grilles/grille-facile2.txt","grilles/grille-facile3.txt","grilles/grille-facile4.txt",
          "grilles/grille-facile5.txt","grilles/grille-facile6.txt"]
Moyen = ["grilles/grille-moyen1.txt","grilles/grille-moyen2.txt","grilles/grille-moyen2.txt","grilles/grille-moyen3.txt","grilles/grille-moyen4.txt"]
Difficile = ["grilles/grille-difficile1.txt","grilles/grille-difficile2.txt","grilles/grille-difficile3.txt"]

# LISTE CONTENANT LES ANCIENNES DERNIERES POSITIONS
liste_segments=[]

# TAILLE DES CASES ET DE LA MARGE
taille_case, taille_marge = 120,10

sommet, sommet1, sommet2 = (0,0), (0,0), (0,0) 

sauvegarde = False
liste_sauvegarde = []                                                 