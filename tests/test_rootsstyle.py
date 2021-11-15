import rootsstyle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def test_version():
    assert rootsstyle.__version__ == "0.1.0"




def test_scatterplot():
    nb_series, nb_dots = 5, 15
    with plt.style.context(rootsstyle.style):
        x = np.arange(start=0, stop=nb_dots, step=1)
        y = np.random.rand(nb_dots, nb_series)
        plt.plot(x, y, linestyle="none", marker="o")
        plt.title("A scatter plot with rootsstyle")
        plt.xlabel(f"range from 0 to {nb_dots}")
        plt.ylabel("random values from 0 to 1")
        plt.legend([f"series {i}" for i in range(nb_series)])
        assert plt.gcf().number == 1
        plt.savefig("images/scatterplot.png", transparent=True)
        plt.close()


def test_barplot_seaborn():
    tips = (
        sns.load_dataset("tips")
        .groupby(["day", "sex"])["total_bill"]
        .mean()
        .reset_index()
    )

    with plt.style.context(rootsstyle.style):
        sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
        plt.title("Average total bill per day per gender")
        plt.xlabel("Day")
        plt.ylabel("Total bill [$]")
        assert plt.gcf().number == 1
        plt.savefig("images/barplot_tips.png", transparent=True)
        plt.close()

def test_barplot_seaborn2():
    diamonds = sns.load_dataset("diamonds")
    diamonds_cut = diamonds.groupby('cut')['price'].count().reset_index().rename(columns={'price': 'count'})
    with plt.style.context(rootsstyle.style):
        sns.barplot(x="cut", y="count", data=diamonds_cut, order=list(diamonds['cut'].unique())[::-1])
        plt.title("Sparkly Stones")
        plt.xlabel("Cut")
        plt.ylabel("Count")
        assert plt.gcf().number == 1
        plt.savefig("images/barplot_sparklystones.png", transparent=True)
        plt.close()

def test_lineplot_seaborn():
    tips = (
        sns.load_dataset("tips")
        .groupby(["day"])["total_bill", "tip"]
        .sum()
        .reset_index()
    )

    with plt.style.context(rootsstyle.style):
        sns.lineplot(x="day", y="total_bill", data=tips)
        sns.lineplot(x="day", y="tip", data=tips)
        plt.title("Total income per day")
        plt.legend(["total bill", "tip"], labelcolor="linecolor")
        plt.xlabel("Day")
        plt.ylabel("USD")
        assert plt.gcf().number == 1
        plt.savefig("images/lineplot.png", transparent=True)
        plt.close()


def test_violin_plot():
    tips = sns.load_dataset("tips")
    with plt.style.context(rootsstyle.style):
        sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips)
        plt.title("Tip distribution per day")
        plt.xlabel("Day")
        plt.ylabel("USD")
        assert plt.gcf().number == 1
        plt.savefig("images/violinplot.png", transparent=True)
        plt.close()