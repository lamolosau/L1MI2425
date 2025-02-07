#exo1

def decomp_facteurs_premiers(n):
    facteurs = []
    diviseur = 2
    while n > 1:
        while n % diviseur == 0:
            facteurs.append(diviseur)
            n //= diviseur
        diviseur += 1
    return facteurs

#exo2

def racine_carree(a, k):
    num = 1
    den = 1
    for _ in range(k):
        num = num * num + a * den * den
        den = 2 * num * den
    return num / den

#exo3

def insere(base, titre, genre, duree):
    base.append({"titre": titre, "genre": genre, "duree": duree})

#exo4

def films_par_genre(genre, base):
    return [film["titre"] for film in base if film["genre"] == genre]

#exo5

def base_genres(base):
    dico = {}
    for film in base:
        if film["genre"] not in dico:
            dico[film["genre"]] = []
        dico[film["genre"]].append(film["titre"])
    return dico

#exo6

def film_plus_long(base):
    return max(base, key=lambda film: film["duree"])["titre"]

#exo7

def presents(liste, base):
    titres_base = {film["titre"] for film in base}
    return [film for film in liste if film in titres_base]

#exo8

def meilleur_film(liste, base):
    return max(liste, key=lambda x: x[1])[0]
