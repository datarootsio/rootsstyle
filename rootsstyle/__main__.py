"""Main file of the rootsstyle repository.
- defines the color palette
- loads the necessary fonts
- defines the style dictionary
"""
import numpy as np
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

colors = {
    "green_light": "#A3F6B4",
    "green_bright": "#3DF29A",
    "green_dark": "#38B580",
    "blue_light": "#BFC6E2",
    "blue_dark": "#445BA7",
    "blue_navy": "#1E2B5F",
    "black": "#212121",
    "gray": "#969696",
    "gray_light": "#C0C2C2",
}

_fonts_dir = Path(__file__).parent.parent.joinpath("fonts")
fonts = {
    "Nunito": Path(_fonts_dir, "Nunito_Sans", "NunitoSans-Regular.ttf"),
    "Arvo": Path(_fonts_dir, "Arvo", "Arvo-Regular.ttf"),
    "Inconsolata": Path(_fonts_dir, "Inconsolata", "Inconsolata-Regular.ttf"),
}
font_entries = [fm.FontEntry(fname=path, name=name) for name, path in fonts.items()]
fm.fontManager.ttflist.extend(font_entries)

# SOURCE: https://matplotlib.org/stable/tutorials/introductory/customizing.html#a-sample-matplotlibrc-file
style = {
    # FONT
    "font.family": "Arvo",
    # TITLE
    "axes.titlelocation": "center",
    "axes.titlesize": 18,
    "axes.titlepad": 12,
    "axes.titlecolor": colors["green_dark"],
    # LABELS
    "axes.labelsize": 12,
    "axes.labelpad": 6,
    "axes.labelcolor": colors["gray"],
    # TICKS
    "xtick.major.width": 0,
    "ytick.major.width": 0,
    "xtick.color": colors["gray"],
    "ytick.color": colors["gray"],
    # AXES
    "axes.linewidth": 1.6,
    "axes.edgecolor": colors["green_dark"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    # LEGEND
    "legend.framealpha": 0,
    # COLORS
    "axes.prop_cycle": mpl.cycler(
        color=[
            colors["green_dark"],
            colors["blue_dark"],
            colors["blue_light"],
            colors["green_light"],
            colors["blue_navy"],
            colors["gray"],
            colors["gray_light"],
            colors["green_bright"],
            colors["black"],
        ],
    ),
}


# Inspiration: https://github.com/nschloe/dufte
def legend_line():
    ax = plt.gca()
    lines = [child for child in ax.get_children() if type(child) == mpl.lines.Line2D]
    if len(lines) == 0:
        return
    # Removing existing legend
    if ax.legend_ is not None:
        ax.legend_ = None
    labels = [line.get_label() for line in lines]
    colors = [line.get_color() for line in lines]

    last_y = [line.get_ydata()[~np.isnan(line.get_ydata())][-1] for line in lines]
    last_x = [line.get_xdata()[~np.isnan(line.get_xdata())][-1] for line in lines]
    targets = [(x * 1.03, y) for x, y in zip(last_x, last_y)]

    for label, (x, y), color in zip(labels, targets, colors):
        plt.text(x, y, label, verticalalignment="center", color=color)


def legend(title=None):
    """Displays the legend to the left of the plot.
    For lineplots, displays each line legend next to the line.
    """
    ax = plt.gca()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    if ax.legend_ is not None:  # e.g. seaborn already set legend
        existing_title = ax.legend_.get_title()._text
        title = title or existing_title
    legend = ax.legend(title=title, loc="center left", bbox_to_anchor=(1, 0.5))
    [text.set_color(colors["gray"]) for text in legend.get_texts()]
    # For seaborn plots, update title
    legend.get_title().set_color(colors["gray"])
    if title is not None:
        legend.set_title(title)


# Inspiration: https://github.com/nschloe/dufte
def ylabel(ylabel: str):
    """Adds a ylabel to the plot at the top of the y-axis

    Args:
        ylabel (str): the name of the label
    """
    ax = plt.gca()
    plt.ylabel(ylabel, horizontalalignment="center").set_rotation(0)
    # sits 3% above top tick
    ax.yaxis.set_label_coords(0, 1.03)
