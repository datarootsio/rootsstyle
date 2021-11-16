"""Main file of the rootsstyle repository.
- defines the color palette
- loads the necessary fonts
- defines the style dictionary
"""
import numpy as np
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
from .utils import is_line_plot
import matplotlib.font_manager as fm

colors = {
    "green_light": "#A3F6B4",
    "green_bright": "#48DF88",
    "green_dark": "#38B580",
    "blue_light": "#BFC6E2",
    "blue_dark": "#445BA7",
    "blue_navy": "#34495D",
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
    ## ***************************************************************************
    ## * FONT                                                                    *
    ## ***************************************************************************
    "font.family": "Arvo",
    ## ***************************************************************************
    ## * TICKS                                                                   *
    ## ***************************************************************************
    "xtick.major.width": 0,
    "ytick.major.width": 0,
    "xtick.color": colors["gray"],
    "ytick.color": colors["gray"],
    ## ***************************************************************************
    ## * AXES                                                                    *
    ## ***************************************************************************
    # DATA COLORS
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
    # EDGES
    "axes.linewidth": 1.6,
    "axes.edgecolor": colors["green_dark"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    # TITLE
    "axes.titlelocation": "center",
    "axes.titlesize": 18,
    "axes.titlepad": 12,
    "axes.titlecolor": colors["green_dark"],
    # LABELS
    "axes.labelsize": 12,
    "axes.labelpad": 6,
    "axes.labelcolor": colors["gray"],
    ## ***************************************************************************
    ## * LEGEND                                                                  *
    ## ***************************************************************************
    "legend.frameon": False,
    ## ***************************************************************************
    ## * SAVING FIGURES                                                          *
    ## ***************************************************************************
    "savefig.transparent": True,
}


# Inspiration: https://github.com/nschloe/dufte
# Inspiration: https://github.com/matplotlib/matplotlib/blob/main/lib/matplotlib/legend.py
def _legend_line(ax, labels=None):
    # Removing existing legend (e.g. default of seaborn)
    if ax.legend_ is not None:
        ax.legend_ = None

    handles = [h for h in mpl.legend._get_legend_handles([ax]) if type(h) == mpl.lines.Line2D]
    colors = [line.get_color() for line in handles]
    if labels is None:
        labels = [line.get_label() for line in handles]

    last_y = [line.get_ydata()[~np.isnan(line.get_ydata())][-1] for line in handles]
    last_x = [line.get_xdata()[~np.isnan(line.get_xdata())][-1] for line in handles]
    targets = [(x * 1.03, y) for x, y in zip(last_x, last_y)]

    for label, (x, y), color in zip(labels, targets, colors):
        plt.text(x, y, label, verticalalignment="center", color=color)


def legend(handles=None, labels=None, title: str = None):
    """Displays the legend to the left of the plot.
    For lineplots, displays each line legend next to the line.

    Args:
        handles (list[mpl.artist.Artist], optional): A list of Artists (lines, patches) to be added to the legend. Defaults to None.
        labels (list[str], optional): A list of labels to show next to the artists.. Defaults to None.
        title (str, optional): The legend's title. Defaults to None.
    """
    ax = plt.gca()
    # Check for existing title
    if ax.legend_ is not None:  # e.g. seaborn already set legend
        title = title or ax.legend_.get_title().get_text()
        labels = labels or [t.get_text() for t in ax.legend_.get_texts()]
        handles = handles or ax.legend_.legendHandles

    if is_line_plot(ax, labels):
        _legend_line(ax, labels)
    else:
        # Shrink box to fit legend to the right
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Set legend
        legend = ax.legend(
            handles=handles,
            labels=labels,
            title=title,
            loc="center left",
            bbox_to_anchor=(1, 0.5),
        )
        [text.set_color(colors["gray"]) for text in legend.get_texts()]
        legend.get_title().set_color(colors["gray"])


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
