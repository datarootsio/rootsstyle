from matplotlib.colors import ListedColormap, LinearSegmentedColormap

layout_colors = {"text": "#969696", "edges": "#38B580"}

palettes = {
    "dataroots-default": ListedColormap(
        name="dataroots-default",
        colors=[
            "#38B580",
            "#445BA7",
            "#BFC6E2",
            "#48DF88",
            "#34495D",
            "#A3F6B4",
            "#212121",
            "#969696",
            "#C0C2C2",
        ],
    ),
    "dataroots-green": LinearSegmentedColormap.from_list(
        name="dataroots-green", colors=["#C3E9D9", "#38B580", "#04441C"], gamma=1.0
    ),
    "dataroots-blue": LinearSegmentedColormap.from_list(
        name="dataroots-blue", colors=["#C9CFE5", "#445BA7", "#19213E"], gamma=1.0
    ),
    "dataroots-blue-to-green": LinearSegmentedColormap.from_list(
        name="dataroots-blue-to-green",
        colors=["#19213E", "#38B580", "#B4E3CF"],
        gamma=1.5,
    ),
    "dataroots-green-to-blue": LinearSegmentedColormap.from_list(
        name="dataroots-green-to-blue",
        colors=["#022108", "#5387C8", "#BFC6E2"],
        gamma=1.5,
    ),
}
