import rootsstyle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

OUTPUT_DIR = "images/plots"


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
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/scatterplot.png")
        plt.close()


def test_lineplot():
    # REGULAR LINEPLOT
    df_cars = sns.load_dataset("mpg")
    df_usa = (
        df_cars[df_cars["origin"] == "usa"].groupby("model_year").mean().reset_index()
    )
    df_japan = (
        df_cars[df_cars["origin"] == "japan"].groupby("model_year").mean().reset_index()
    )
    df_europe = (
        df_cars[df_cars["origin"] == "europe"]
        .groupby("model_year")
        .mean()
        .reset_index()
    )
    with plt.style.context(rootsstyle.style):
        sns.lineplot(x="model_year", y="mpg", data=df_usa, label="USA")
        sns.lineplot(x="model_year", y="mpg", data=df_japan, label="Japan")
        sns.lineplot(x="model_year", y="mpg", data=df_europe, label="Europe")
        rootsstyle.legend()
        rootsstyle.ylabel("mpg")
        plt.xlabel("model year")
        plt.title("Cars")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/lineplot_cars.png")
        plt.close()

    # LINEPLOT WITH HUE PALETTE
    df_flights = sns.load_dataset("flights")
    with plt.style.context(rootsstyle.style):
        sns.lineplot(
            x="month",
            y="passengers",
            data=df_flights,
            hue="year",
            palette=rootsstyle.palettes["dataroots-green"][:12],
        )
        rootsstyle.legend()
        rootsstyle.ylabel("passengers")
        plt.xlabel("month")
        plt.title("Flights")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/lineplot_green.png")
        plt.close()

        sns.lineplot(
            x="month",
            y="passengers",
            data=df_flights,
            hue="year",
            palette=rootsstyle.palettes["dataroots-blue"][:12],
        )
        rootsstyle.legend()
        rootsstyle.ylabel("passengers")
        plt.xlabel("month")
        plt.title("Flights")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/lineplot_blue.png")
        plt.close()

    # LOGARITMIC LINEPLOT + MULTILINE LEGENDS
    # https://github.com/karlrupp/microprocessor-trend-data
    df_cpus = pd.read_csv("tests/cpus.csv")
    with plt.style.context(rootsstyle.style):
        g = sns.lineplot(
            x="year", y="transistors", data=df_cpus, label="transistors\n[1000s]"
        )
        g = sns.lineplot(x="year", y="watts", data=df_cpus, label="watts")
        g = sns.lineplot(
            x="year", y="frequency", data=df_cpus, label="frequency\n[MHz]"
        )
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
        plt.savefig(f"{OUTPUT_DIR}/lineplot_cpus.png")
        plt.close()


def test_barplot():
    df_cars = sns.load_dataset("mpg")
    df_cars["model_year"] = "' " + df_cars["model_year"].astype(str)
    with plt.style.context(rootsstyle.style):
        sns.barplot(x="model_year", y="mpg", data=df_cars, hue="origin", ci=None)
        rootsstyle.ylabel("mpg")
        plt.xlabel("model year")
        rootsstyle.legend()
        plt.title("Cars")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/barplot_mpg.png")
        plt.close()

        sns.barplot(x="model_year", y="horsepower", data=df_cars, hue="origin", ci=None)
        rootsstyle.ylabel("horsepower")
        plt.xlabel("model year")
        rootsstyle.legend()
        plt.title("Cars")
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/barplot_horsepower.png")
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
        plt.savefig(f"{OUTPUT_DIR}/violinplot.png")
        plt.close()


def test_pieplot():
    df_penguins = sns.load_dataset("penguins")
    df_penguins = df_penguins.groupby("species").size().to_frame("count").reset_index()
    with plt.style.context(rootsstyle.style):
        plt.pie(df_penguins["count"], labels=df_penguins["species"], autopct="%.0f%%")
        plt.title("Pinguin distribution")
        rootsstyle.legend()
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/pieplot.png")
        plt.close()
