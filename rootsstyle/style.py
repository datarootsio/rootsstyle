"""One of the main files of rootsstyle. This file defines the styling aspect enable either
globally using 'plt.style.use(rootsstyle.style)' or within a context manager using 'plt.style.context(rootsstyle.style)'.
"""
import matplotlib as mpl

from ._colors import layout_colors, palettes

# DOCS: https://matplotlib.org/stable/tutorials/introductory/customizing.html#a-sample-matplotlibrc-file
style = {
    # ***************************************************************************
    # * FONT                                                                    *
    # ***************************************************************************
    "font.family": "Arvo",
    "font.size": 10,  # used for line legend
    "text.color": layout_colors["text"],
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
