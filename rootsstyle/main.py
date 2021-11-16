"""Main file of the rootsstyle repository.
- defines the style dictionary
- defines the optional extra functionalities
"""
from .fonts import fonts
from .colors import colors
from .utils import is_line_plot
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Add fonts to matplotlib global fontManager
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
    """Displays the legend next to the line

    Args:
        ax ([type]): [description]
        labels ([type], optional): [description]. Defaults to None.
    """
    # Removing existing legend (e.g. default of seaborn)
    if ax.legend_ is not None:
        ax.legend_ = None

    handles = [
        h for h in mpl.legend._get_legend_handles([ax]) if type(h) == mpl.lines.Line2D
    ]
    colors = [h.get_color() for h in handles]
    if labels is None:
        labels = [h.get_label() for h in handles]

    last_y = [h.get_ydata()[~np.isnan(h.get_ydata())][-1] for h in handles]
    last_x = [h.get_xdata()[~np.isnan(h.get_xdata())][-1] for h in handles]
    targets = [(x * 1.03, y) for x, y in zip(last_x, last_y)]

    for label, (x, y), color in zip(labels, targets, colors):
        plt.text(x, y, label, verticalalignment="center", color=color)
    return {"labels": labels, "handles": handles}


def legend(handles=None, labels=None, title = None):
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
        legend = _legend_line(ax, labels)
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
    return {"labels": labels, "handles": handles}


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
