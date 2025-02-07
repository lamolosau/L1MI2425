#exo1

class CompteBancaire:
    def __init__(self, nom="Djibril LAKEL", solde=0):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        if somme <= self.solde:
            self.solde -= somme
        else:
            print("retrait impossible le solde est insuffisant.")

    def affiche(self):
        print(self.nom)
        print(self.solde)

def programme_principal_compte():
    compte1 = CompteBancaire("Michu", 800)
    compte1.depot(350)
    compte1.retrait(200)
    compte1.affiche()

    compte2 = CompteBancaire("Blanchard")
    compte2.depot(25)
    compte2.affiche()

programme_principal_compte()

#exo2

class Voiture:
    def __init__(self, nom, couleur, vitesse=0):
        self.nom = nom
        self.couleur = couleur
        self.vitesse = vitesse

    def accelere(self, inc):
        if inc > 0:
            nouvelle_vitesse = self.vitesse + inc
            if nouvelle_vitesse > 130:
                self.vitesse = 130
            else:
                self.vitesse = nouvelle_vitesse

    def freine(self, dec):
        if dec > 0:
            nouvelle_vitesse = self.vitesse - dec
            if nouvelle_vitesse < 0:
                self.vitesse = 0
            else:
                self.vitesse = nouvelle_vitesse

    def __str__(self):
        if self.vitesse == 0:
            return f"la voiture {self.nom} de couleur {self.couleur} est à l'arret."
        else:
            return f"la voiture {self.nom} de couleur {self.couleur} roule à {self.vitesse} km/h."

    def affiche(self):
        print(self.nom)
        print(self.couleur)
        print(self.vitesse)

def programme_principal_voiture():
    voiture1 = Voiture("Renault", "Jaune")
    voiture1.accelere(50)
    print(voiture1)

    voiture1.freine(30)
    print(voiture1)

    voiture1.accelere(150)
    print(voiture1)

programme_principal_voiture()

#exo3

class Carte:
    def __init__(self, couleur, hauteur, est_atout=False):
        if couleur in ["trèfle", "carreau", "coeur", "pique"]:
            self.couleur = couleur
        else:
            raise ValueError("couleur invalide")

        if hauteur in list(range(7, 11)) + ["Valet", "Dame", "Roi", "As"]:
            self.hauteur = hauteur
        else:
            raise ValueError("hauteur invalide")

        self.atout = est_atout

    def affiche(self):
        return f"{self.hauteur} de {self.couleur}"

    def get_couleur(self):
        return self.couleur

    def get_hauteur(self):
        return self.hauteur

    def get_nbre_points(self):
        points_hors_atout = {7: 0, 8: 0, 9: 0, "Valet": 2, "Dame": 3, "Roi": 4, 10: 10, "As": 11}
        points_atout = {7: 0, 8: 0, 9: 14, "Valet": 20, "Dame": 3, "Roi": 4, 10: 10, "As": 11}
        if self.atout:
            return points_atout.get(self.hauteur, 0)
        else:
            return points_hors_atout.get(self.hauteur, 0)

    def est_plus_grand(self, carte):
        if self.atout and not carte.atout:
            return True
        if not self.atout and carte.atout:
            return False

        points_self = self.get_nbre_points()
        points_carte = carte.get_nbre_points()
        return points_self > points_carte

    def est_egal(self, carte):
        return self.hauteur == carte.hauteur and self.couleur == carte.couleur and self.atout == carte.atout

#LAKEL Djibril
