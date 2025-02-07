import random

#exo1

class puissancequatre:
    def __init__(self):
        self.nb_lignes = 6
        self.nb_colonnes = 7
        self.plateau = [[-1 for _ in range(self.nb_colonnes)] for _ in range(self.nb_lignes)]
        self.carac = ["o", "x"]
        self.dernier_coup = (-1, -1)

#exo2

    def carac(self, joueur):
        return self.carac[joueur]

#exo3

    def __str__(self):
        affichage = "   " + "   ".join(str(i) for i in range(self.nb_colonnes)) + "\n"
        affichage += "  +" + "---+" * self.nb_colonnes + "\n"
        for ligne in self.plateau:
            affichage += "  | " + " | ".join(" " if case == -1 else self.carac[case] for case in ligne) + " |\n"
            affichage += "  +" + "---+" * self.nb_colonnes + "\n"
        return affichage


#exo4

    def colonne_valide(self, col):
        return 0 <= col < self.nb_colonnes and self.plateau[0][col] == -1

#exo5

    def pose_colonne(self, choix, joueur):
        if not self.colonne_valide(choix):
            return False
        for i in range(self.nb_lignes-1, -1, -1):
            if self.plateau[i][choix] == -1:
                self.plateau[i][choix] = joueur
                self.dernier_coup = (i, choix)
                return True
        return False

#exo6

    def coords_valide(self, lig, col):
        return 0 <= lig < self.nb_lignes and 0 <= col < self.nb_colonnes

#exo7

    def compte_valeur(self, lig, col, val, inc_lig, inc_col):
        compteur = 0
        lig += inc_lig
        col += inc_col
        while self.coords_valide(lig, col) and self.plateau[lig][col] == val:
            compteur += 1
            lig += inc_lig
            col += inc_col
        return compteur

#exo8

    def partie_finie(self):
        if self.dernier_coup == (-1, -1):
            return False
        lig, col = self.dernier_coup
        val = self.plateau[lig][col]
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for inc_lig, inc_col in directions:
            if self.compte_valeur(lig, col, val, inc_lig, inc_col) + self.compte_valeur(lig, col, val, -inc_lig, -inc_col) >= 3:
                return True
        return False









if __name__ == "__main__":
    p4 = puissancequatre()
    joueur = random.randint(0, 1)
    
    while not p4.partie_finie():
        print(p4)
        print("aux", p4.carac[joueur], "de jouer")
        choix = int(input("dans quelle colonne voulez-vous jouer ? "))
        res = p4.pose_colonne(choix, joueur)
        if not res:
            print("non, ce n’est pas possible.")
        else:
            joueur = (joueur + 1) % 2

    print(p4)
    print("partie finie. bravo")