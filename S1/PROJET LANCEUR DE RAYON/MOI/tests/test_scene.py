from projetl1.scene import lire_scene

def manage_scene(filename,output,nb_pixels,nb_objs,nb_lights):
    scene = lire_scene(filename)
    assert scene['output'] == output
    size = scene['size']
    assert size[0]*size[1] == nb_pixels
    assert len(scene['spheres'])+len(scene['plans'])+len(scene['triangles']) == nb_objs
    assert len(scene['directional'])+len(scene['point']) == nb_lights

def test_scene1():
    manage_scene('TEST3/test1.scene','mascene.png',307200,1,2)

def test_scene2():
    manage_scene('TEST3/test2.scene','mascene.png',307200,1,2)

def test_scene3():
    manage_scene('TEST3/test3.scene','mascene.png',307200,3,2)

def test_scene4():
    manage_scene('TEST3/test4.scene','mascene.png',307200,6,2)

def test_scene5():
    manage_scene('TEST3/test5.scene','mascene.png',307200,1,1)

def test_scene5():
    manage_scene('TEST3/test6.scene','mascene.png',786432,4,2)
