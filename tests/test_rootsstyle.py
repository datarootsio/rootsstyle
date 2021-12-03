import rootsstyle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def test_version():
    assert rootsstyle.__version__ == "0.1.9"


def test_empty_plot():
    with plt.style.context(rootsstyle.style):
        plt.plot([], [])
        assert plt.gcf().number == 1
        plt.close()


def test_legend():
    df_penguins = sns.load_dataset("penguins")
    df_flights = sns.load_dataset("flights")
    df_flights["month"] = pd.to_datetime(df_flights["month"], format="%b").dt.month
    with plt.style.context(rootsstyle.style):
        sns.scatterplot(
            x="body_mass_g",
            y="flipper_length_mm",
            marker="+",
            data=df_penguins,
            hue="sex",
        )
        legend = rootsstyle.legend()
        assert len(legend.items()) == 2
        assert set(legend.keys()) == set(["labels", "handles"])
        assert set(legend["labels"]) == set(["Male", "Female"])
        assert plt.gcf().number == 1
        plt.close()

        sns.lineplot(
            x="month",
            y="passengers",
            data=df_flights,
            hue="year",
            palette="dataroots-green",
            legend="full",
        )
        legend = rootsstyle.legend()
        assert len(legend.items()) == 2
        assert set(legend.keys()) == set(["labels", "handles"])
        assert set(legend["labels"]) == set(map(str, list(range(1949, 1961))))
        assert plt.gcf().number == 1
        plt.close()

        sns.lineplot(
            x="month",
            y="passengers",
            data=df_flights,
            hue="year",
            palette="dataroots-blue",
            legend=False,
        )
        legend = rootsstyle.legend(labels=list(map(str, list(range(1949, 1961)))))
        assert len(legend.items()) == 2
        assert set(legend.keys()) == set(["labels", "handles"])
        assert set(legend["labels"]) == set(map(str, list(range(1949, 1961))))
        assert plt.gcf().number == 1
        plt.close()


def test_ylabel():
    df_penguins = sns.load_dataset("penguins")
    df_penguins = df_penguins.groupby(["island", "species"]).size().to_frame("count").reset_index()
    with plt.style.context(rootsstyle.style):
        sns.barplot(x="island", y="count", data=df_penguins, hue="species")
        rootsstyle.ylabel("penguins")
        assert plt.gca().get_ylabel() == "penguins"
        assert plt.gca().yaxis.label._rotation == 0
        assert plt.gcf().number == 1
        plt.close()
