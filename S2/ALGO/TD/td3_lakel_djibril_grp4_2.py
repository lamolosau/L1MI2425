# -*- coding: utf-8 -*-
"""td3_LAKEL_Djibril_grp4-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cc6MV1nqYR2oYV2-7duvMxrsq0UJ4eml
"""

class Etudiant:
  def __init__(self, prenom, nom, formation):
    self.nom = nom
    self.prenom = prenom
    self.formation = formation
    self.notes = {}
    self.est_diplome = False
    self.saisie_possible = True

  def nom(self):
    return self.nom

  def prenom(self):
    return self.prenom

  def est_diplome(self):
    return self.est_diplome

  def ajoute_note(self, matiere, note):
    if self.saisie_possible:
      if matiere in self.notes:
        self.notes[matiere].append(note)
      else:
        self.notes[matiere] = [note]
      return True
    else:
      return False

  def moyenne_matiere(self, matiere):
    if matiere in self.notes:
      return sum(self.notes[matiere]) / len(self.notes[matiere])
    else:
      return None

  def les_matieres(self):
      return list(self.notes.keys())

  def stop_saisie_notes(self):
    self.saisie_possible = False

  def __str__(self):
    return f"{self.prenom} {self.nom}"

  def moyenne_generale(self, coefs):
      total_weighted_score = 0
      total_coefficients = 0

      for matiere, score in self.notes.items():
        if matiere in coefs:
          coefficient = coefs[matiere]
          total_weighted_score += score * coefficient
          total_coefficients += coefficient
        else:
            raise ValueError(f"pas de coef pour: {matiere}")

      if total_coefficients == 0:
            raise ValueError("total coef 0")

      return total_weighted_score / total_coefficients

  def est_diplome(self, coefs):
      return self.moyenne_generale(coefs) >= 10

e1 = Etudiant("Fanny","Bravo","Semestre 2 - Lic. Informatique")
print(e1.ajoute_note("anglais",18))
print(e1.ajoute_note("anglais",19))
print(e1.ajoute_note("algo",17))
print(e1.moyenne_matiere("algo"))
print(e1.moyenne_matiere("anglais"))
print(e1.les_matieres())
print(str(e1))
e1.stop_saisie_notes()

class Formation:
    def __init__(self, nom, matieres_coefs):
        self.nom = nom
        self.etudiants = []
        self.matieres_coefs = matieres_coefs
        self.notes_saisies = True

    def ajoute_etudiant(self, nom, prenom):
        etudiant = Etudiant(prenom, nom, self)
        self.etudiants.append(etudiant)

    def __str__(self):
        return f"Formation: {self.nom}, Nombre d'étudiants: {len(self.etudiants)}"

    def affiche_formation(self):
        print(f"Nom de la formation: {self.nom}")
        print("Matières et coefficients:")
        for matiere, coef in self.matieres_coefs.items():
            print(f"- {matiere}: {coef}")
        print(f"Nombre d'étudiants: {len(self.etudiants)}")

    def affiche_etudiants(self):
        print("Liste des étudiants:")
        for etudiant in self.etudiants:
            print(f"- {etudiant}")

    def ajoute_note_etudiant(self, num_etudiant, matiere, note):
        if self.notes_saisies:
            if 0 <= num_etudiant < len(self.etudiants):
                etudiant = self.etudiants[num_etudiant]
                return etudiant.ajoute_note(matiere, note)
            else:
                print("Numéro d'étudiant invalide.")
                return False
        else:
            print("La saisie des notes est stoppée.")
            return False

    def calcule_diplomes(self):
        self.notes_saisies = False
        total_moyenne = 0
        for etudiant in self.etudiants:
          etudiant.stop_saisie_notes()
          total_moyenne += etudiant.moyenne_generale(self.matieres_coefs)

        if len(self.etudiants) > 0:
          return total_moyenne / len(self.etudiants)
        else:
            return 0

    def les_diplomes(self):
        diplomes = []
        for etudiant in self.etudiants:
          if etudiant.est_diplome(self.matieres_coefs):
            diplomes.append((etudiant.prenom, etudiant.nom))
        return diplomes