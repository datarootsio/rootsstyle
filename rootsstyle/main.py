"""Main file of the rootsstyle repository.
- defines the style dictionary
- defines the optional extra functionalities
"""
from .fonts import fonts
from .colors import layout_colors, palettes
from .utils import is_line_plot, get_dataline_handles, get_linelegend_ypositions
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# Register fonts in global FontManager
font_entries = [fm.FontEntry(fname=path, name=name) for name, path in fonts.items()]
fm.fontManager.ttflist.extend(font_entries)
# Register colormaps in global ColorMap manager
[mpl.cm.register_cmap(cmap_name, cmap) for cmap_name, cmap in palettes.items()]

# DOCS: https://matplotlib.org/stable/tutorials/introductory/customizing.html#a-sample-matplotlibrc-file
style = {
    # ***************************************************************************
    # * FONT                                                                    *
    # ***************************************************************************
    "font.family": "Arvo",
    "font.size": 10,  # used for line legend
    # ***************************************************************************
    # * TICKS                                                                   *
    # ***************************************************************************
    "xtick.minor.width": 0,
    "ytick.minor.width": 0,
    "xtick.major.width": 0.2,
    "ytick.major.width": 0.2,
    "xtick.color": layout_colors["text"],
    "ytick.color": layout_colors["text"],
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    # ***************************************************************************
    # * AXES                                                                    *
    # ***************************************************************************
    # DATA COLORS
    "axes.prop_cycle": mpl.cycler(
        color=palettes["dataroots-default"].colors,
    ),
    # EDGES
    "axes.linewidth": 1.6,
    "axes.edgecolor": layout_colors["edges"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    # TITLE
    "axes.titlelocation": "center",
    "axes.titlesize": 18,
    "axes.titlepad": 12,
    "axes.titlecolor": layout_colors["edges"],
    # LABELS
    "axes.labelsize": 12,
    "axes.labelpad": 6,
    "axes.labelcolor": layout_colors["text"],
    # ***************************************************************************
    # * LEGEND                                                                  *
    # ***************************************************************************
    "legend.frameon": False,
    "legend.fontsize": 10,
    # ***************************************************************************
    # * SAVING FIGURES                                                          *
    # ***************************************************************************
    "savefig.transparent": True,
}


# Inspiration: https://github.com/nschloe/dufte
# Inspiration: https://github.com/matplotlib/matplotlib/blob/main/lib/matplotlib/legend.py
def _legend_line(ax, labels=None):
    """Displays the legendentries next to the line in the same color as the line

    Args:
        ax (mpl.axes.Axes): Axes object of the graph
        labels (list[str], optional): list of labels to use. Defaults to None.
    Returns:
        dict: a dictionary containing entries for 'labels' and 'handles' used by the legend.
    """
    # Removing existing legend (e.g. default of seaborn)
    handles = get_dataline_handles(ax)
    colors = [h.get_color() for h in handles]
    if labels is None or len(labels) != len(handles):
        labels = [h.get_label() for h in handles]

    targets = get_linelegend_ypositions(ax, handles, labels)

    for label, (x, y), color in zip(labels, targets, colors):
        plt.text(x, y, label, verticalalignment="center", color=color)
    return {"labels": labels, "handles": handles}


def legend(handles=None, labels=None, title=None):
    """Displays the legend to the left of the plot.
    For lineplots, displays each line legend next to the line.

    Args:
        handles (list[mpl.artist.Artist], optional): list of Artists (lines, patches) to be added to the legend.
            Defaults to None.
        labels (list[str], optional): A list of labels to show next to the artists.
            Defaults to None.
        title (str, optional): The legend's title.
            Defaults to None.
    """
    ax = plt.gca()
    # Check for existing title
    if ax.legend_ is not None:  # e.g. seaborn already set legend
        title = title or ax.legend_.get_title().get_text()
        handles = handles or ax.legend_.legendHandles
        labels = labels or [t.get_text() for t in ax.legend_.get_texts()]
        ax.legend_ = None

    if is_line_plot(ax, labels):
        legend = _legend_line(ax, labels)
    else:
        # Set legend
        legend = ax.legend(
            handles=handles,
            labels=labels,
            title=title,
            loc="center left",
            bbox_to_anchor=(1, 0.5),
        )
        [
            text.set_color(
                layout_colors["text"],
            )
            for text in legend.get_texts()
        ]
        legend.get_title().set_color(
            layout_colors["text"],
        )
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
