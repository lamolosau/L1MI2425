import pytest
import os
from projetl1.compare import compare_files
from projetl1.lanceurrayons import generer_image

testdata = []
content = os.listdir('TEST5')
for f in content:
    if f.endswith('.test'):
        testdata.append(f)

@pytest.mark.parametrize("scene_file",testdata)
def test_image_generation(scene_file):
    output_file = scene_file.replace('.test','.png')
    generer_image(f'TEST5/{scene_file}')
    nb_diff,_ = compare_files(output_file,f'TEST5/{output_file}')
    assert nb_diff <= 2