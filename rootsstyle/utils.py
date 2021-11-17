import numpy as np
import scipy.optimize
import matplotlib as mpl
import matplotlib.pyplot as plt

# pyplot.legend() -> gca().legend()
# axes.legend() -> legend._parse_legend_args()
# legend._parse_legend_args() -> labels!=None and handles==None:
def get_dataline_handles(ax):
    """Returns the handles that correspond to datalines

    Args:
        ax (Axes): the axis of the graph to look in
        handles (list[mpl.artist.Artist], optional): A list of Artists (lines, patches) to be added to the legend. Defaults to None.
        
    Returns:
        list[handle]: list of handles that correspond to datalines
    """
    return [
        h for h in mpl.legend._get_legend_handles([ax]) if type(h) == mpl.lines.Line2D and not np.all(np.isnan(h.get_ydata()))
    ]


def is_line_plot(ax, labels=None) -> bool:
    """Determines whether the plot is a pure line plot or if it contains other types of data visualizations.

    Args:
        ax (mpl.axes.Axes): Axes object of the graph
        labels (list[str], optional): list of labels to use. Defaults to None.

    Returns:
        bool: True if the plot is a pure lineplot, False otherwise
    """
    handles = get_dataline_handles(ax)
    if len(handles) == 0:
        return False  # No lines in plot
    if labels != None and len(handles) != len(labels):
        # Some plots (e.g. violin plots) also use Line2D object for some data (e.g. errorlines))
        return False
    # Filter scatterplots
    linestyles = [h._linestyle for h in handles]
    return "None" not in linestyles  


def get_handle_color(handle):
    """Returns the color of the handle

    Args:
        handle ([type]): The handle that contains the color property

    Returns:
        str: color of the handle
    """
    if type(handle) == mpl.lines.Line2D:
        return handle.get_color()
    if type(handle) == mpl.patches.Rectangle:
        return handle.get_facecolor()


def get_linelegend_ypositions(ax, handles):
    """Calculates the positions of the legendentries.
    Ensures that there is no vertical overlap between entires.

    src: https://github.com/nschloe/dufte/blob/fa94fcc7277993942a1cbb909301105cd154644a/src/dufte/main.py#L96

    Args:
        ax (mpl.axes.Axes): Axes object of the graph
        handles (list[mpl.lines.Line2D]): list of handles representing the datalines we are making a legend for.

    Returns:
        list[(float, float)]: a list of (x,y) coordinates for the legend entries 
    """
    fontsize_inches = mpl.rcParams["font.size"] / 72
    fig_height_inches = plt.gcf().get_size_inches()[1]
    yaxis_height_inches = (ax.get_position().y1 - ax.get_position().y0) * fig_height_inches
    yaxis_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    min_distance = fontsize_inches / yaxis_height_inches * yaxis_range

    # Find position heights and adjust so that there is no overlap
    last_y = [h.get_ydata()[~np.isnan(h.get_ydata())][-1] for h in handles]
    idx = np.argsort(last_y)
    targets = np.sort(last_y)
    n = len(targets)

    y0_min = targets[0] - n * min_distance
    A = np.tril(np.ones([n, n]))
    b = targets - (y0_min + np.arange(n) * min_distance)

    out, _ = scipy.optimize.nnls(A, b)
    sol = np.cumsum(out) + y0_min + np.arange(n) * min_distance
    idx2 = np.argsort(idx)
    last_y = sol[idx2]

    # Add x-coordinates to get position next to last datapoint
    last_x = [h.get_xdata()[~np.isnan(h.get_xdata())][-1] for h in handles]
    xaxis_range = ax.get_xlim()[1] - ax.get_xlim()[0]
    targets = [(x + xaxis_range*0.03, y) for x, y in zip(last_x, last_y)]

    return targets