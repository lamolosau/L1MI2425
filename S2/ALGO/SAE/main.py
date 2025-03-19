import tkinter as tk
import random

class Case:
    def __init__(self, couleur):
        self.couleur = couleur
    
    def get_couleur(self):
        return self.couleur
    
    def set_couleur(self, couleur):
        self.couleur = couleur
    
    def supprimer(self):
        self.couleur = -1
    
    def est_vide(self):
        return self.couleur == -1

class ModeleSame:
    def __init__(self, nblig=10, nbcol=15, nbcouleurs=3):
        self.nblig = nblig
        self.nbcol = nbcol
        self.nbcouleurs = nbcouleurs
        self.mat = [[Case(random.randint(0, nbcouleurs - 1)) for _ in range(nbcol)] for _ in range(nblig)]
    
    def supprimer_case(self, i, j):
        if 0 <= i < self.nblig and 0 <= j < self.nbcol:
            self.mat[i][j].supprimer()
    
    def reinit(self):
        self.mat = [[Case(random.randint(0, self.nbcouleurs - 1)) for _ in range(self.nbcol)] for _ in range(self.nblig)]

class VueSame(tk.Tk):
    def __init__(self, modele):
        super().__init__()
        self.modele = modele
        self.title("SameGame")
        self.case_size = 40
        self.canvas = tk.Canvas(self, width=self.modele.nbcol * self.case_size, height=self.modele.nblig * self.case_size)
        self.canvas.pack()
        self.bouton_reset = tk.Button(self, text="Nouvelle Partie", command=self.reinit)
        self.bouton_reset.pack()
        self.canvas.bind("<Button-1>", self.clic)
        self.afficher_plateau()
    
    def afficher_plateau(self):
        self.canvas.delete("all")
        couleurs = ["red", "blue", "green"]
        for i in range(self.modele.nblig):
            for j in range(self.modele.nbcol):
                couleur = self.modele.mat[i][j].get_couleur()
                fill_color = "white" if couleur == -1 else couleurs[couleur]
                self.canvas.create_rectangle(j * self.case_size, i * self.case_size,
                                             (j + 1) * self.case_size, (i + 1) * self.case_size,
                                             fill=fill_color, outline="black")
    
    def clic(self, event):
        j = event.x // self.case_size
        i = event.y // self.case_size
        self.modele.supprimer_case(i, j)
        self.afficher_plateau()
    
    def reinit(self):
        self.modele.reinit()
        self.afficher_plateau()



















if __name__ == "__main__":
    modele = ModeleSame()
    vue = VueSame(modele)
    vue.mainloop()