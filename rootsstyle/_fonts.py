from pathlib import Path

_fonts_dir = Path(__file__).parent.parent.joinpath("fonts")
fonts = {
    "Nunito": Path(
        _fonts_dir,
        "Nunito_Sans",
        "NunitoSans-Regular.ttf",
    ),
    "Arvo": Path(
        _fonts_dir,
        "Arvo",
        "Arvo-Regular.ttf",
    ),
    "Inconsolata": Path(
        _fonts_dir,
        "Inconsolata",
        "Inconsolata-Regular.ttf",
    ),
}
