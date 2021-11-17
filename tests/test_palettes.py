import rootsstyle
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def test_palette():
    plt.style.use(rootsstyle.style)
    palettes = rootsstyle.palettes
    max_colors = max([len(colors) for colors in palettes.values()])
    _, axes = plt.subplots(nrows=len(palettes.items()))

    for p, (palette_name, palette_colors) in enumerate(palettes.items()):
        ax = axes[p]
        ax.set_xlim(0, max_colors)
        for i in range(len(palette_colors)):
            ax.add_patch(
                patches.Rectangle(
                    (i, 0), width=1, height=1, linewidth=0, facecolor=palette_colors[i]
                )
            )
        ax.set_title(palette_name)
        ax.axis("off")

    plt.tight_layout()
    plt.savefig("images/palette.png", transparent=True)
    plt.close()
