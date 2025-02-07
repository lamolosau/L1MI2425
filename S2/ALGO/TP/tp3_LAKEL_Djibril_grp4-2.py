import random

#exo1

class case:
    def __init__(self):
        self.valeur = 0
        self.cache = True

    def est_cache(self):
        return self.cache

    def est_visible(self):
        return not self.cache

    def est_bombe(self):
        return self.valeur == -1

    def est_vide(self):
        return self.valeur == 0

    def incremente_valeur(self):
        if not self.est_bombe():
            self.valeur += 1

    def montre_toi(self):
        self.cache = False

    def __str__(self):
        if self.cache:
            return "-"
        if self.est_bombe():
            return "*"
        if self.est_vide():
            return " "
        return str(self.valeur)

#exo2

class demineur:
    def __init__(self, nb_lig=10, nb_col=20):
        self.nb_lig = nb_lig
        self.nb_col = nb_col
        self.plateau = [[case() for _ in range(nb_col)] for _ in range(nb_lig)]

    def affiche_ligne_traits(self):
        print("  +" + "---+" * self.nb_col)

    def affiche_ligne(self, lig):
        ligne = "|"
        for c in range(self.nb_col):
            ligne += str(self.plateau[lig][c]) + "|"
        print(ligne)

    def affiche_plateau(self):
        print("   " + "  ".join(f"{i:2}" for i in range(self.nb_col)))
        self.affiche_ligne_traits()
        for l in range(self.nb_lig):
            ligne = f"{l:2} |"
            for c in range(self.nb_col):
                ligne += f" {self.plateau[l][c]} |"
            print(ligne)
            self.affiche_ligne_traits()

    def pose_bombes(self, nb_bombes=15):
        for _ in range(nb_bombes):
            while True:
                l = random.randint(0, self.nb_lig - 1)
                c = random.randint(0, self.nb_col - 1)
                if not self.plateau[l][c].est_bombe():
                    self.plateau[l][c].valeur = -1
                    self.mettre_a_jour_voisins(l, c)
                    break

    def mettre_a_jour_voisins(self, l, c):
        for i in range(max(0, l - 1), min(self.nb_lig, l + 2)):
            for j in range(max(0, c - 1), min(self.nb_col, c + 2)):
                self.plateau[i][j].incremente_valeur()

    def partie_finie(self, l, c):
        return self.plateau[l][c].est_bombe() or all(
            not self.plateau[i][j].est_cache() for i in range(self.nb_lig) for j in range(self.nb_col) if not self.plateau[i][j].est_bombe()
        )

    def montre(self, l, c):
        self.montre_case(l, c)
        self.affiche_plateau()

    def montre_case(self, l, c):
        if not self.plateau[l][c].est_visible():
            self.plateau[l][c].montre_toi()
            if self.plateau[l][c].est_bombe():
                print("boum!!")
            elif self.plateau[l][c].est_vide():
                for i in range(max(0, l - 1), min(self.nb_lig, l + 2)):
                    for j in range(max(0, c - 1), min(self.nb_col, c + 2)):
                        self.montre_case(i, j)

#exo3

def jouer():
    jeu = demineur()
    jeu.pose_bombes()
    jeu.affiche_plateau()
    
    while True:
        l = int(input("ligne: "))
        c = int(input("colonne: "))
        if 0 <= l < jeu.nb_lig and 0 <= c < jeu.nb_col:
            jeu.montre(l, c)
            if jeu.partie_finie(l, c):
                print("partie terminee")
                break
        else:
            print("coordonnees invalides")

jouer()
