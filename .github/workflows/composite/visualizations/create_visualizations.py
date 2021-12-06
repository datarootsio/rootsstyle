import os
import sys
import math
import shutil
import logging
import itertools
import rootsstyle
from PIL import Image
import matplotlib as mpl
from pathlib import Path
from tests import test_plots
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from inspect import getmembers, isfunction

OUTPUT_DIR = "images/"
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
TEMP_DIR = "temp_images"
Path(TEMP_DIR).mkdir(parents=True, exist_ok=True)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def create_all_test_plots():
    """Creates all plotting functions defined in tests/test_plots.py"""
    plot_functions = getmembers(test_plots, isfunction)
    for function_name, function in plot_functions:
        logging.info(f"Calling {function_name}")
        function(output_dir=TEMP_DIR)


def create_example_grid():
    """Creates the grid of plots that is shown at the top of the README file"""
    logging.info(f"Creating grid of example plots")
    plt.style.use(rootsstyle.style)

    images = []
    for (dirpath, _, filenames) in os.walk(TEMP_DIR):
        images.extend([os.path.join(dirpath, filename) for filename in filenames])

    nb_images = len(images)
    nb_cols = 3
    nb_rows = math.ceil(nb_images / 3)
    _, axes = plt.subplots(nrows=nb_rows, ncols=nb_cols, figsize=(30, 30))
    indices = list(itertools.product(list(range(nb_rows)), list(range(nb_cols))))
    for i, image in enumerate(images):
        x, y = indices[i]
        ax = axes[x, y]
        image = Image.open(image)
        ax.imshow(image)
        ax.axis("off")
    for i in range(len(images), nb_cols * nb_rows):
        x, y = indices[i]
        ax = axes[x, y]
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(Path(OUTPUT_DIR) / "examples.png")
    plt.close()
    shutil.rmtree(TEMP_DIR)


def create_example_plots():
    """Creates the plots that are shown in the USAGE-EXAMPLES section"""
    plt.style.use(rootsstyle.style)

    logging.info(f"Creating example lineplot")
    y = [3, 8, 1, 10]
    y2 = [8, 3, 10, 2]
    plt.plot(y, label="y")
    plt.plot(y2, label="y2", linestyle="dotted")
    rootsstyle.ylabel("yvalues")
    plt.xlabel("x-label")
    rootsstyle.legend()
    plt.title("Example lineplot")
    plt.savefig(Path(OUTPUT_DIR) / "example_lineplot.png")
    plt.close()

    logging.info(f"Creating example barplot")
    languages = ["C", "C++", "Java", "Python", "PHP"]
    students = [23, 17, 35, 29, 12]
    plt.bar(languages, students)
    plt.xlabel("Language")
    rootsstyle.show_bar_values()
    plt.title("Example barplot")
    plt.savefig(Path(OUTPUT_DIR) / "example_barplot.png")
    plt.close()


def create_palette_plot():
    logging.info(f"Creating image of palettes")
    plt.style.use(rootsstyle.style)
    mpl_cmaps = mpl.colormaps._cmaps
    dataroots_cmaps = dict()
    for cmap_name, cmap in mpl_cmaps.items():
        if "dataroots" in cmap_name:
            dataroots_cmaps[cmap_name] = cmap
    max_colors = 256.0
    _, axes = plt.subplots(nrows=len(dataroots_cmaps.items()))

    for p, (cmap_name, cmap) in enumerate(dataroots_cmaps.items()):
        ax = axes[p]
        ax.set_xlim(0, max_colors)
        width = max_colors / cmap.N
        for i in range(cmap.N):
            ax.add_patch(
                patches.Rectangle(
                    (i * width, 0),
                    width=width,
                    height=1,
                    linewidth=0,
                    facecolor=cmap(i),
                )
            )
        ax.set_title(cmap_name)
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(Path(OUTPUT_DIR) / "palette.png")
    plt.close()


if __name__ == "__main__":
    create_all_test_plots()
    create_example_grid()
    create_example_plots()
    create_palette_plot()
