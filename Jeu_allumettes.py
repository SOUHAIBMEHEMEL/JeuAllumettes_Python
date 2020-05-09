#########################################################################
#
#                   REALISE PAR: MEHEMEL SOUHAIB 2CS-SIL1
#
#########################################################################
# nom : jeu_ordi
# valeurs entree : nb_allum et prise_max, nombre d'allumette en jeu et
# nombre d'allumette que l'on peut prendre au plus.
# valeurs sortie : prise, nombre d'allumettes prises.
# fonction : retourne la meilleure prise à faire
#########################################################################
def jeu_ordi(nb_allum, prise_max):
    s = prise_max + 1
    t = (nb_allum - s) % (prise_max + 1)
    while (t != 0):
        s -= 1
        t = (nb_allum - s) % (prise_max + 1)
    prise = s - 1
    if (prise == 0):
        prise = 1
    print("l'ordi en prend : ", prise)
    return prise


#########################################################################
def affichage(nb_restant):
    i = 0
    for i in range(0, nb_restant):
        print(" 0 ", end=""),
    print(" ")
    for i in range(0, nb_restant):
        print(" | ", end=""),
    print(" ")


#########################################################################
# nom : main
# fonction : initialiser le jeu et l'organiser.
#########################################################################
def main():
    # initialisation des variables.
    nb_max_d = 0  # nbre d'allumettes maxi au départ
    nb_allu_max = 1000  # nbre d'allumettes maxi que l'on peut tirer au maxi
    nb_allu_res = 0  # nbre d'allumettes restantes
    prise = 0  # nbre d'allumettes prises par le joueur
    qui = -1  # qui joue? 0=User --- 1=PC

    # verification pour l'initialisation.
    while (nb_max_d < 10 or nb_max_d > 60):
        try:
            nb_max_d = int(input("Entrez un nombre max d'allumette au depart entre 10 et 60: "))
        except:
            print("saisie incorrecte")

    # initialisation de nombre de prise max.
    while (nb_allu_max > nb_max_d):
        try:
            nb_allu_max = int(input("Entrez un nombre max d'allumette a prendre a chaque fois: "))
        except:
            print("saisie incorrecte")

    # mise a jour du nombre d'allumette en jeu.
    qui = int(input("qui commence? (0: user/1: pc): "))
    nb_allu_res = nb_max_d
    while (nb_allu_res > 0):
        if (qui == 0):
            prise = int(input("le nombre que vous voulez prendre: "))
            nb_allu_res -= prise
            print("nombre restant:  ", nb_allu_res)
            affichage(nb_allu_res)
            qui = 1
        else:
            prise = jeu_ordi(nb_allu_res, nb_allu_max)
            nb_allu_res -= prise
            print("nombre restant:  ", nb_allu_res)
            affichage(nb_allu_res)
            qui = 0

    if (qui == 0):
        print("USER a gagne")
    else:
        print("PC a gagne")


main()