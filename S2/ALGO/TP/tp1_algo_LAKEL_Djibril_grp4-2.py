import random
import string

def ajoute_livre(auteur, annee, titre, prix, quantite, genre, catalogue):
    if genre not in catalogue:
        catalogue[genre] = []
    nouveau_livre = {"auteur": auteur, "annee": annee, "titre": titre, "prix": prix, "quantite": quantite}
    catalogue[genre].append(nouveau_livre)

def estPresent(catalogue, titre):
    for genre in catalogue:
        for livre in catalogue[genre]:
            if livre["titre"] == titre:
                return True
    return False

def affiche_livre(livre):
    for cle, valeur in livre.items():
        print(f'"{cle}": {valeur}')

def changer_prix(livre, prix):
    livre["prix"] = prix

def ajoute_quantite(catalogue, titre, qte):
    for genre in catalogue:
        for livre in catalogue[genre]:
            if livre["titre"] == titre:
                livre["quantite"] += qte

def livres_auteur(catalogue, auteur):
    resultats = []
    for genre in catalogue:
        for livre in catalogue[genre]:
            if livre["auteur"] == auteur:
                resultats.append(livre["titre"])
    return resultats

def livres_annee(catalogue, date):
    resultats = []
    for genre in catalogue:
        for livre in catalogue[genre]:
            if livre["annee"] == date:
                resultats.append(livre)
    return resultats

def les_plus_chers(catalogue):
    max_prix = 0
    resultats = []
    for genre in catalogue:
        for livre in catalogue[genre]:
            if livre["prix"] > max_prix:
                max_prix = livre["prix"]
                resultats = [livre]
            elif livre["prix"] == max_prix:
                resultats.append(livre)
    return resultats

def genres_litteraires(catalogue, auteur):
    resultats = []
    for genre in catalogue:
        for livre in catalogue[genre]:
            if livre["auteur"] == auteur and genre not in resultats:
                resultats.append(genre)
    return resultats

def commande(catalogue, liste_livres):
    for titre, quantite in liste_livres.items():
        for genre in catalogue:
            for livre in catalogue[genre]:
                if livre["titre"] == titre:
                    if livre["quantite"] < quantite:
                        return False
    for titre, quantite in liste_livres.items():
        for genre in catalogue:
            for livre in catalogue[genre]:
                if livre["titre"] == titre:
                    livre["quantite"] -= quantite
                    if livre["quantite"] == 0:
                        catalogue[genre].remove(livre)
    return True

def permuteListe(uneListe):
    for i in range(len(uneListe)):
        j = random.randint(0, len(uneListe) - 1)
        uneListe[i], uneListe[j] = uneListe[j], uneListe[i]

def dictPerm():
    lettres = list(string.ascii_uppercase)
    permuteListe(lettres)
    return {lettres[i]: lettres[(i + 1) % len(lettres)] for i in range(len(lettres))}

def crypte(txt, perm):
    resultat = ""
    for char in txt:
        if char in perm:
            resultat += perm[char]
        else:
            resultat += char
    return resultat

def invertDict(perm):
    return {v: k for k, v in perm.items()}

def decrypte(txt, perm):
    perm_inverse = invertDict(perm)
    return crypte(txt, perm_inverse)

def affiche_menu():
    print("1 : liste des codes disponibles.")
    print("2 : creer un nouveau code.")
    print("3 : crypter un texte.")
    print("4 : decrypter un texte.")
    print("0 : quitter l'application.")
    return int(input("votre choix : "))

def afficher_les_codes(codes):
    for nom, code in codes.items():
        print(f"{nom} : {code}")

def ajouter_un_code(codes):
    nom = input("donnez le nom de votre nouveau code : ")
    codes[nom] = dictPerm()

def crypter_un_texte(codes):
    afficher_les_codes(codes)
    nom = input("nom du code choisi : ")
    texte = input("texte a crypter : ")
    print("le texte crypte est :", crypte(texte, codes[nom]))

def decrypter_un_texte(codes):
    afficher_les_codes(codes)
    nom = input("nom du code a choisir : ")
    texte = input("texte a decrypter : ")
    print("le texte decrypte est :", decrypte(texte, codes[nom]))

def programme_principal():
    codes = {}
    while True:
        choix = affiche_menu()
        if choix == 1:
            afficher_les_codes(codes)
        elif choix == 2:
            ajouter_un_code(codes)
        elif choix == 3:
            crypter_un_texte(codes)
        elif choix == 4:
            decrypter_un_texte(codes)
        elif choix == 0:
            print("bye")
            break
        else:
            print("choix invalide.")

#LAKEL Djibril
