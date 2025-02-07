from projetl1.compare import compare_files

def test_meme_image():
    nb_diff,_ = compare_files("TEST1/image1.png","TEST1/image1.png")
    assert nb_diff == 0
    nb_diff,_ = compare_files("TEST1/image2.png","TEST1/image2.png")
    assert nb_diff == 0

def test_images_differentes():
    nb_diff,image_diff = compare_files("TEST1/image1.png","TEST1/image2.png")
    assert nb_diff == 879
    image_diff.save("diff.png")
    nb_diff,image_diff = compare_files("TEST1/diff.png","diff.png")
    assert nb_diff == 0
