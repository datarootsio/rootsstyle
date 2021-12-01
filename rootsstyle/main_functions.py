"""One of the main files of rootsstyle. This file defines the added functionalities:
- rootsstyle.legend()
- rootsstyle.ylabel()
"""
from ._fonts import fonts
from ._colors import layout_colors, palettes
from ._utils import is_line_plot, get_dataline_handles, get_linelegend_ypositions
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Register fonts in global FontManager
font_entries = [fm.FontEntry(fname=path, name=name) for name, path in fonts.items()]
fm.fontManager.ttflist.extend(font_entries)
# Register colormaps in global ColorMap manager
[mpl.cm.register_cmap(cmap_name, cmap) for cmap_name, cmap in palettes.items()]


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
        _legend_line(ax, labels)
    else:
        # Set legend
        ax.legend(
            handles=handles,
            labels=labels,
            title=title,
            loc="center left",
            bbox_to_anchor=(1, 0.5),
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


def show_bar_values(remove_y_axis=True, fontsize=12, position="below", fmt="{:.2f}"):
    ax = plt.gca()

    if remove_y_axis:
        plt.tick_params(
            axis="y", which="both", left=False, right=False, labelleft=False
        )
        plt.grid(False)
        plt.margins(x=0)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

    for rect in ax.patches:
        height = rect.get_height()
        ypos = height * 0.98 if position == "below" else height * 1.01
        ax.text(
            rect.get_x() + rect.get_width() / 2,
            ypos,
            fmt.format(height),
            size=fontsize,
            weight="bold",
            ha="center",
            va="top" if position == "below" else "bottom",
            color="white" if position == "below" else layout_colors["text"],
        )
