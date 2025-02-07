import sys

def init_scene() -> dict:
    '''cree une scene vide'''
    scene = {
        'size': (640, 480),
        'output': 'output.png',
        'camera': {'look_from': (0, 0, 0), 'look_at': (0, 0, 0), 'up': (0, 0, 0), 'fov': 0},
        'ambient': (0, 0, 0),
        'diffuse': (0, 0, 0),
        'specular': (0, 0, 0),
        'shininess': 0,
        'directional': [],
        'point': [],
        'vertex': [],
        'triangles': [],
        'spheres': [],
        'plans': []
    }
    return scene

def gerer_ligne(scene: dict, l: str):
    '''gere une ligne du fichier'''
    l = l.strip().split()
    if len(l) > 0 and l[0] == "size":
        # ici j'ai galéré un peu pour bien extraire les valeurs
        largeur = int(l[1])
        hauteur = int(l[2])
        scene['size'] = (largeur, hauteur)
    elif len(l) > 0 and l[0] == "output":
        scene['output'] = l[1]
    elif len(l) > 0 and l[0] == "camera":
        # là j'avais essayé avec moins de paramètres mais ça marchait pas
        lx, ly, lz = float(l[1]), float(l[2]), float(l[3])
        ux, uy, uz = float(l[4]), float(l[5]), float(l[6])
        mx, my, mz = float(l[7]), float(l[8]), float(l[9])
        fov = float(l[10])
        scene['camera']['look_from'] = (lx, ly, lz)
        scene['camera']['look_at'] = (ux, uy, uz)
        scene['camera']['up'] = (mx, my, mz)
        scene['camera']['fov'] = fov
    elif len(l) > 0 and l[0] == "ambient":
        r, g, b = float(l[1]), float(l[2]), float(l[3])
        scene['ambient'] = (r, g, b)
    elif len(l) > 0 and l[0] == "diffuse":
        r, g, b = float(l[1]), float(l[2]), float(l[3])
        scene['diffuse'] = (r, g, b)
    elif len(l) > 0 and l[0] == "specular":
        r, g, b = float(l[1]), float(l[2]), float(l[3])
        scene['specular'] = (r, g, b)
    elif len(l) > 0 and l[0] == "shininess":
        # ici j'ai mis int direct parce que c'est forcément un entier
        scene['shininess'] = int(l[1])
    elif len(l) > 0 and l[0] == "directional":
        x, y, z, r, g, b = map(float, l[1:])
        scene['directional'].append(((x, y, z), (r, g, b)))
    elif len(l) > 0 and l[0] == "point":
        x, y, z, r, g, b = map(float, l[1:])
        scene['point'].append(((x, y, z), (r, g, b)))
    elif len(l) > 0 and l[0] == "vertex":
        x, y, z = map(float, l[1:])
        scene['vertex'].append((x, y, z))
    elif len(l) > 0 and l[0] == "tri":
        i1, i2, i3 = map(int, l[1:])
        maxverts = len(scene['vertex'])
        if i1 < maxverts and i2 < maxverts and i3 < maxverts:
            scene['triangles'].append((i1, i2, i3))
        else:
            print("erreur dans les indices du triangle")  # ça m'a aidé à comprendre d'où venait l'erreur
    elif len(l) > 0 and l[0] == "sphere":
        x, y, z, r = map(float, l[1:])
        scene['spheres'].append(((x, y, z), r))
    elif len(l) > 0 and l[0] == "plane":
        x, y, z, u, v, w = map(float, l[1:])
        scene['plans'].append(((x, y, z), (u, v, w)))

def lire_scene(fichier_scene: str):
    '''lit un fichier et retourne la scene'''
    scene = init_scene()
    fichier = open(fichier_scene, "r")
    for ligne in fichier:
        # la je boucle sur chaque ligne du fichier
        gerer_ligne(scene, ligne)
    fichier.close()
    return scene

if __name__ == '__main__':
    if len(sys.argv) == 2:
        scene = lire_scene(sys.argv[1])
        print(scene['output'])  # affiche le fichier de sortie
        print(scene['size'][0] * scene['size'][1])  # calcule le nombre de pixels
        print(len(scene['triangles']) + len(scene['spheres']) + len(scene['plans']))  # compte les objets
        print(len(scene['directional']) + len(scene['point']))  # compte les lumières
    else:
        print("utilisation : python3 scene.py <fichier_de_scene>")
