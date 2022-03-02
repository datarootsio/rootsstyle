import math
from typing import List

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from ._nnls import nnls


# pyplot.legend() -> gca().legend()
# axes.legend() -> legend._parse_legend_args()
# legend._parse_legend_args() -> labels!=None and handles==None:
def get_dataline_handles(
    ax: mpl.axes.Axes,
):
    """Returns the handles that correspond to datalines

    Args:
        ax (Axes): the axis of the graph to look in
    Returns:
        list[handle]: list of handles that correspond to datalines
    """
    return [
        h
        for h in mpl.legend._get_legend_handles([ax])
        if type(h) == mpl.lines.Line2D and not np.all(np.isnan(h.get_ydata()))
    ]


def is_line_plot(ax: mpl.axes.Axes, labels: List[str] = None) -> bool:
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
    if labels is not None and len(handles) != len(labels):
        # Some plots (e.g. violin/bar plots) also use Line2D object for some data (e.g. errorlines))
        return False
    # Filter scatterplots
    linestyles = [h._linestyle for h in handles]
    return "None" not in linestyles


def get_linelegend_ypositions(
    ax: mpl.axes.Axes,
    handles: List[mpl.artist.Artist],
    labels: List[str] = None,
):
    """Calculates the positions of the legendentries.
    Ensures that there is no vertical overlap between entires.
    https://github.com/nschloe/dufte?src/dufte/main.py

    Args:
        ax (mpl.axes.Axes): Axes object of the graph
        handles (list[mpl.lines.Line2D]): list of handles representing the datalines we are making a legend for.
        labels (list[str], optional): list of labels to use.
            Defaults to None.
    Returns:
        list[(float, float)]: a list of (x,y) coordinates for the legend entries
    """
    fontsize_inches = mpl.rcParams["font.size"] / 72
    fig_height_inches = plt.gcf().get_size_inches()[1]
    yaxis_height_inches = (
        ax.get_position().y1 - ax.get_position().y0
    ) * fig_height_inches
    if ax.get_yscale() == "log":
        yaxis_range = math.log10(ax.get_ylim()[1]) - math.log10(
            ax.get_ylim()[0]
        )
    else:
        yaxis_range = ax.get_ylim()[1] - ax.get_ylim()[0]
    spacing_between_lines = 1.1
    line_height = (
        fontsize_inches
        / yaxis_height_inches
        * yaxis_range
        * spacing_between_lines
    )

    # Find position heights and adjust so that there is no overlap
    last_y = [h.get_ydata()[~np.isnan(h.get_ydata())][-1] for h in handles]
    if ax.get_yscale() == "log":
        last_y = [math.log10(y) for y in last_y]
    idx = np.argsort(last_y)
    targets = np.sort(last_y)
    labels = np.array(labels)[idx]
    n = len(targets)
    lines_away_from_first_label = np.arange(
        n,
        dtype=float,
    )
    for i in range(
        1,
        len(labels),
    ):
        distance_to_prev_label = (
            2 + f"{labels[i-1]}_{labels[i]}".count("\n")
        ) / 2
        lines_away_from_first_label[i] = (
            lines_away_from_first_label[i - 1] + distance_to_prev_label
        )

    y0_min = targets[0] - lines_away_from_first_label[-1] * line_height
    A = np.tril(np.ones([n, n]))
    b = targets - (y0_min + lines_away_from_first_label * line_height)

    out = nnls(A, b)
    sol = np.cumsum(out) + y0_min + lines_away_from_first_label * line_height
    idx2 = np.argsort(idx)
    last_y = sol[idx2]
    if ax.get_yscale() == "log":
        last_y = [10**y for y in last_y]

    # Add x-coordinates to get position next to last datapoint
    last_x = [h.get_xdata()[~np.isnan(h.get_xdata())][-1] for h in handles]
    xaxis_range = ax.get_xlim()[1] - ax.get_xlim()[0]
    targets = [
        (
            x + xaxis_range * 0.03,
            y,
        )
        for x, y in zip(
            last_x,
            last_y,
        )
    ]

    return targets
