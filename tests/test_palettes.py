import rootsstyle
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def test_palette():
    plt.style.use(rootsstyle.style)
    mpl_cmaps = mpl.colormaps._cmaps
    dataroots_cmaps = dict()
    for cmap_name, cmap in mpl_cmaps.items():
        if "dataroots" in cmap_name:
            dataroots_cmaps[cmap_name]=cmap
    max_colors = 256.0
    _, axes = plt.subplots(nrows=len(dataroots_cmaps.items()))

    for p, (cmap_name, cmap) in enumerate(dataroots_cmaps.items()):
        ax = axes[p]
        ax.set_xlim(0, max_colors)
        width = max_colors /  cmap.N
        for i in range(cmap.N):
            ax.add_patch(
                patches.Rectangle(
                    (i*width, 0),
                    width=width,
                    height=1,
                    linewidth=0,
                    facecolor=cmap(i),
                )
            )
        ax.set_title(cmap_name)
        ax.axis("off")

    plt.tight_layout()
    plt.savefig("images/palette.png", transparent=True)
    plt.close()
