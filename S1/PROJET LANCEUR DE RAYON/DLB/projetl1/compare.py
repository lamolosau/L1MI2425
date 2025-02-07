import sys
from PIL import Image

# Les fonctions à utiliser
# Image.open() pour obtenir un objet image à partir d'un fichier
# Image.new() pour créer une nouvelle image vide (noire)
# image.load() pour obtenir un tableau de pixels à partir d'une image
# image.save() pour sauvegarde une image dans un fichier
# image.size pour connaître la taille d'une image

def compare_files(filename1:str, filename2:str) -> tuple[int,Image]:
    '''Compare deux fichiers image PNG et retourne le nombre de pixels différents.
    Si ce nombre de pixels est supérieur à 0, alors l'image représentant la différence point à point de l'image est disponible dans le second membre du tuple'''
    raise NotImplementedError
    

if __name__ == '__main__':
    if (len(sys.argv)==3):
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]

        nb_diff,image_diff = compare_files(filename1,filename2)

        if (nb_diff>0):
            image_diff.save("diff.png")

        if (nb_diff<1000):
            print("OK")
        else:
            print("KO")
        
        print(nb_diff)

    else:
        print("Usage : python3 compare.py file1 file2")