import rootsstyle
import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt

TEMP_DIR = "temp_images"
Path(TEMP_DIR).mkdir(parents=True, exist_ok=True)


def test_scatterplot():
    df_penguins = sns.load_dataset("penguins")
    with plt.style.context(rootsstyle.style):
        sns.scatterplot(
            x="body_mass_g",
            y="flipper_length_mm",
            marker="+",
            data=df_penguins,
            hue="species",
        )
        rootsstyle.legend()
        rootsstyle.ylabel("flipper length\n[mm]")
        plt.xlabel("body mass [g]")
        plt.title("Penguins")
        plt.text(4550, 185, "Chunky Mike", fontdict={"color": rootsstyle.colors[0]})
        plt.text(5400, 232, "Big Bob", fontdict={"color": rootsstyle.colors[2]})
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "scatterplot.png")
        plt.close()


def test_lineplot():
    # REGULAR LINEPLOT
    df_cars = sns.load_dataset("mpg")
    df_cars = df_cars.groupby(["origin", "model_year"]).mean().reset_index()
    with plt.style.context(rootsstyle.style):
        sns.lineplot(
            x="model_year",
            y="mpg",
            data=df_cars,
            hue="origin",
            palette=sns.color_palette("dataroots-default", as_cmap=True).colors[:3],
        )
        rootsstyle.legend()
        rootsstyle.ylabel("mpg")
        plt.xlabel("model year")
        plt.title("Cars")
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "lineplot_cars.png")
        plt.close()

    # LINEPLOT WITH HUE PALETTE
    df_flights = sns.load_dataset("flights")
    with plt.style.context(rootsstyle.style):
        sns.lineplot(
            x="month",
            y="passengers",
            data=df_flights,
            hue="year",
            palette="dataroots-green",
            legend="full",
        )
        rootsstyle.legend()
        rootsstyle.ylabel("passengers")
        plt.xlabel("month")
        plt.title("Flights")
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "lineplot_green.png")
        plt.close()

        sns.lineplot(
            x="month",
            y="passengers",
            data=df_flights,
            hue="year",
            palette="dataroots-blue",
            legend="full",
        )
        rootsstyle.legend()
        rootsstyle.ylabel("passengers")
        plt.xlabel("month")
        plt.title("Flights")
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "lineplot_blue.png")
        plt.close()

    # LOGARITMIC LINEPLOT + MULTILINE LEGENDS
    # https://github.com/karlrupp/microprocessor-trend-data
    df_cpus = pd.read_csv("tests/data/cpus.csv")
    with plt.style.context(rootsstyle.style):
        g = sns.lineplot(x="year", y="transistors", data=df_cpus, label="transistors\n[1000s]")
        g = sns.lineplot(x="year", y="watts", data=df_cpus, label="watts")
        g = sns.lineplot(x="year", y="frequency", data=df_cpus, label="frequency\n[MHz]")
        g = sns.lineplot(x="year", y="cores", data=df_cpus, label="logical\ncores")
        g = sns.lineplot(
            x="year",
            y="single_core_performance",
            data=df_cpus,
            label="single thread\nperformance\n[SpecINT x10³",
        )
        g.set_yscale("log")
        plt.ylabel("")
        plt.xlabel("Year")
        plt.title("48 Years of Microprocessor Trends")
        rootsstyle.legend()
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "lineplot_cpus.png")
        plt.close()


def test_barplot():
    df_tips = sns.load_dataset("tips")
    df_cars = sns.load_dataset("mpg")
    df_cars["model_year"] = "' " + df_cars["model_year"].astype(str)
    with plt.style.context(rootsstyle.style):
        sns.barplot(x="model_year", y="mpg", data=df_cars, hue="origin", ci=None)
        rootsstyle.ylabel("mpg")
        plt.xlabel("model year")
        rootsstyle.legend()
        plt.title("Cars")
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "barplot_mpg.png")
        plt.close()

        sns.barplot(x="day", y="total_bill", hue="sex", data=df_tips, ci=None)
        rootsstyle.ylabel("total bill")
        plt.xlabel("day")
        rootsstyle.legend()
        rootsstyle.show_bar_values(position="below")
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "barplot_tips_below.png")
        plt.close()

        sns.barplot(x="day", y="total_bill", hue="sex", data=df_tips, ci=None)
        rootsstyle.ylabel("total bill")
        plt.xlabel("day")
        rootsstyle.legend()
        rootsstyle.show_bar_values(position="above", fmt="{:.2f}")
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "barplot_tips_above.png")
        plt.close()


def test_violinplot():
    df_tips = sns.load_dataset("tips")
    with plt.style.context(rootsstyle.style):
        sns.violinplot(x="day", y="total_bill", hue="smoker", data=df_tips)
        plt.title("Tip income")
        plt.xlabel("Day")
        rootsstyle.ylabel("USD")
        rootsstyle.legend()
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "violinplot.png")
        plt.close()


def test_pieplot():
    df_penguins = sns.load_dataset("penguins")
    df_penguins = df_penguins.groupby("species").size().to_frame("count").reset_index()
    with plt.style.context(rootsstyle.style):
        plt.pie(df_penguins["count"], labels=df_penguins["species"], autopct="%.0f%%")
        plt.title("Penguin distribution")
        rootsstyle.legend()
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "pieplot.png")
        plt.close()


def test_heatmap():
    df_flights = sns.load_dataset("flights")
    df_flights = df_flights.pivot("month", "year", "passengers")
    with plt.style.context(rootsstyle.style):
        sns.heatmap(data=df_flights, cmap="dataroots-blue-to-green")
        rootsstyle.ylabel("month")
        plt.title("Passengers in flights")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "heatmap_blue_to_green.png")
        plt.close()

        sns.heatmap(data=df_flights, cmap="dataroots-green-to-blue")
        rootsstyle.ylabel("month")
        plt.title("Passengers in flights")
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.savefig(Path(TEMP_DIR) / "heatmap_green_to_blue.png")
        plt.close()