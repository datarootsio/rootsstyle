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
    "green_light": "#52BE7F",
    "green_dark": "#27AE60",
    "blue_dark": "#2980B9",
    "blue_light": "#3498DB",
    "blue_navy": "#34495D",
    "gray": "#969696",
    "gray_light": "#bfc7e2",
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
    "axes.titlelocation": "left",
    "axes.titlesize": 18,
    "axes.titlepad": 12,
    "axes.titlecolor": colors["green_light"],
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
    "axes.edgecolor": colors["green_light"],
    "axes.spines.top": False,
    "axes.spines.right": False,
    # LEGEND
    "legend.framealpha": 0,
    # COLORS
    "axes.prop_cycle": mpl.cycler(
        color=[
            colors["green_light"],
            colors["blue_dark"],
            colors["green_dark"],
            colors["blue_navy"],
            colors["blue_light"],
            colors["gray_light"],
        ],
    ),
}

#Inspiration: https://github.com/nschloe/dufte
def line_legend(ax=None):
    ax = ax or plt.gca()
    lines = [child for child in ax.get_children() if type(child)==mpl.lines.Line2D]
    if len(lines)==0:
        return
    labels = [line.get_label() for line in lines]
    colors = [line.get_color() for line in lines]

    targets = [ line.get_ydata()[~np.isnan(line.get_ydata())][-1] for line in lines]
    ymax = ax.get_ylim()[1]
    targets = [min(target, ymax) for target in targets]

    axis_to_data = ax.transAxes + ax.transData.inverted()
    xpos = axis_to_data.transform([1.03, 1.0])[0]
    for label, ypos, color in zip(labels, targets, colors):
        plt.text(xpos, ypos, label, verticalalignment="center", color=color)

def legend(title=None):
    """Displays the legend to the left of the plot.
    For lineplots, displays each line legend next to the line.
    """
    ax = plt.gca()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    if ax.legend_ is not None: #e.g. seaborn already set legend
        existing_title = ax.legend_.get_title()._text 
        title = title or existing_title
    legend = ax.legend(title=title, loc='center left', bbox_to_anchor=(1, 0.5))
    [text.set_color(colors['gray']) for text in legend.get_texts()]
    #For seaborn plots, update title
    legend.get_title().set_color(colors['gray'])
    if title is not None:
        legend.set_title(title)