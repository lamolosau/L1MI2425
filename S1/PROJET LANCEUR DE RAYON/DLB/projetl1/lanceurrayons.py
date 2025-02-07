import sys
import math
from PIL import Image
from projetl1.scene import lire_scene
from projetl1.triplets import add
from projetl1.triplets import mul
from projetl1.triplets import sub
from projetl1.triplets import dot
from projetl1.triplets import times
from projetl1.triplets import cross
from projetl1.triplets import hat


def calculer_image(scene_descr: dict) -> Image :
    '''calcule l'image à partir de sa description'''
    raise NotImplementedError

def generer_image(fichier_scene):
    '''génère une image à partir d'un fichier de description de scène'''
    scene_descr = lire_scene(fichier_scene)
    image = calculer_image(scene_descr)
    image.save(scene_descr['output'])

if __name__ == '__main__':
    if len(sys.argv)==2:
        generer_image(sys.argv[1])
    else:
        print('Usage : python3 lanceurrayons.py <scene>')