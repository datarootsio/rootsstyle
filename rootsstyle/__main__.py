"""Main file of the rootsstyle repository. 
- defines the color palette
- loads the necessary fonts
- defines the style dictionary
"""

from pathlib import Path
import matplotlib as mpl
import matplotlib.font_manager as fm

colors = {
    "green_light": "52BE7F",
    "green_dark": "27AE60",
    "blue_dark": "2980B9",
    "blue_light": "3498DB",
    "blue_navy": "34495D",
    "gray": "969696",
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
    "legend.framealpha": 0.9,
    # COLORS
    "axes.prop_cycle": mpl.cycler(
        color=[
            colors["green_light"],
            colors["blue_dark"],
            colors["green_dark"],
            colors["blue_navy"],
            colors["blue_light"],
        ],
    ),
}
