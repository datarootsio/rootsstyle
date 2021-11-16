import numpy as np
import matplotlib as mpl

# pyplot.legend() -> gca().legend()
# axes.legend() -> legend._parse_legend_args()
# legend._parse_legend_args() -> labels!=None and handles==None:


def get_line_handles(ax):
    return [
        h for h in mpl.legend._get_legend_handles([ax]) if type(h) == mpl.lines.Line2D
    ]


def is_line_plot(ax: mpl.axes.Axes, labels) -> bool:
    """Determines whether the plot is a pure line plot or if it contains other types of data visualizations.

    Args:
        ax (mpl.axes.Axes): Axes object of the graph

    Returns:
        bool: True if the plot is a pure lineplot, False otherwise
    """
    handles = get_line_handles(ax)
    if len(handles) == 0:
        return False  # No lines in plot
    if labels != None and len(handles) != len(labels):
        return (
            False  # Some plots (e.g. violin plots also use Line2D object for some data)
        )
    linestyles = [h._linestyle for h in handles]
    return "None" not in linestyles  # linestyle 'None' is used for scatterplots


def get_handle_color(handle):
    if type(handle) == mpl.lines.Line2D:
        return handle.get_color()
    if type(handle) == mpl.patches.Rectangle:
        return handle.get_facecolor()
