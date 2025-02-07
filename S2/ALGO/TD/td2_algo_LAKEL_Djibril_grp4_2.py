#exo1

class domino:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def valeur(self):
        return self.a + self.b

    def renverse(self):
        self.a, self.b = self.b, self.a

    def __str__(self):
        return f"[{self.a}|{self.b}]"

    def affiche_points(self):
        print(self)

    def possible_apres(self, do):
        return self.b == do.a or self.b == do.b

#exo2

def affiche_dominos(liste):
    print(" - ".join(str(d) for d in liste))

#exo3

def nbre_points(liste):
    return sum(d.valeur() for d in liste)

#exo4

def cree_jeu_dominos():
    return [domino(i, j) for i in range(7) for j in range(i, 7)]
