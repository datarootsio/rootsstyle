import math
import rootsstyle
import itertools
import matplotlib.pyplot as plt
from PIL import Image
from tests.test_plots import OUTPUT_DIR as INPUT_DIR
import os

def plot_example_images():
    """Plots a 3x3 grid of example images
    """
    plt.style.use(rootsstyle.style)

    images = []
    for (dirpath, _, filenames) in os.walk(INPUT_DIR):
        images.extend([os.path.join(dirpath, filename) for filename in filenames])

    nb_images = len(images)
    nb_cols = 3
    nb_rows = math.ceil(nb_images/3)
    fig, axes = plt.subplots(nrows=nb_rows, ncols=nb_cols, figsize=(15,8))
    indices = list(itertools.product(list(range(nb_cols)), list(range(nb_rows))))
    for i, image in enumerate(images):
        y, x = indices[i]
        ax = axes[x,y]
        image = Image.open(image)
        ax.imshow(image)
        ax.axis("off")

    plt.tight_layout()
    plt.savefig("images/examples.png")


plot_example_images()