"""Main file of the rootsstyle repository. 
- defines the color palette
- loads the necessary fonts
- defines the style dictionary
"""

from pathlib import Path
import matplotlib as mpl
import matplotlib.font_manager as fm

colors = {
    "green_light": "38b580",
    "green_dark": "005921",
    "blue_dark": "445ba7",
    "blue_light": "bfc7e2",
    "black": "212121",
    "gray": "969696",
    "pink": "ff6361",
    "yellow": "ffa600",
}

_fonts_dir = Path(__file__).parent.parent.joinpath("fonts")
fonts = {
    "Nunito": Path(_fonts_dir, "Nunito_Sans", "NunitoSans-Regular.ttf"),
    "Arvo": Path(_fonts_dir, "Arvo", "Arvo-Regular.ttf"),
    "Inconsolata": Path(_fonts_dir, "Inconsolata", "Inconsolata-Regular.ttf"),
}
font_entries = [fm.FontEntry(fname=path, name=name) for name, path in fonts.items()]
fm.fontManager.ttflist.extend(font_entries)

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
            colors["blue_light"],
            colors["green_dark"],
            colors["black"],
            colors["yellow"],
        ],
    ),
}