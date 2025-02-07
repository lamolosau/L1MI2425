import sys

def init_scene() -> dict:
    '''Crée une structure de scène vide.'''
    scene = {
        'size' : (640,480),
        'output' : 'output.png',
        'camera' : { 'look_from':(0,0,0),'look_at':(0,0,0),'up':(0,0,0),'fov':0},
        'ambient' : (0,0,0),
        'diffuse' : (0,0,0),
        'specular' : (0,0,0),
        'shininess' : 0,
        'directional' :  [],
        'point' : [],
        'vertex' : [],
        'triangles' : [],
        'spheres' : [],
        'plans' : []
    }
    return scene


def gerer_ligne(scene:dict,l:str):
    '''Gère une ligne du fichier de description de scène'''
    raise NotImplementedError

def lire_scene(fichier_scene:str):
    scene = init_scene()
    fichier = open(fichier_scene, "r")
    for ligne in fichier:
        gerer_ligne(scene,ligne)
    fichier.close()
    return scene

if __name__ == '__main__':
    if len(sys.argv)==2:
        scene = lire_scene(sys.argv[1])
        print(scene['output'])
        print(scene['size'][0]*scene['size'][1])
        print(len(scene['triangles'])+len(scene['spheres'])+len(scene['plans']))
        print(len(scene['directional'])+len(scene['point']))
    else: 
        print('Usage : python3 scene.py <fichier_de_scene>')
