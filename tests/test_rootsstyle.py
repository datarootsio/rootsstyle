import rootsstyle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

output_dir = "images"

def test_version():
    assert rootsstyle.__version__ == "0.1.2"


def test_empty_plot():
    with plt.style.context(rootsstyle.style):
        plt.plot([], [], linestyle="none")
        plt.title("Empty scatterplot")
        assert plt.gcf().number == 1
        plt.close()

        plt.plot([], [])
        plt.title("Empty lineplot")
        assert plt.gcf().number == 1
        plt.close()


def test_scatterplot():
    nb_series = len(rootsstyle.colors)
    nb_dots = 100//nb_series
    with plt.style.context(rootsstyle.style):
        x = np.arange(start=0, stop=nb_dots, step=1)
        y = np.random.rand(nb_dots, nb_series)
        plt.plot(
            x,
            y,
            linestyle="none",
            marker="o",
            label=[f"series {i}" for i in range(nb_series)],
        )
        plt.title("Randoms")
        plt.xlabel("Index")
        rootsstyle.ylabel("Value")
        rootsstyle.legend()
        assert plt.gcf().number == 1
        plt.savefig(f"{output_dir}/scatterplot.png")
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
        plt.title("Total income")
        plt.xlabel("Day")
        rootsstyle.ylabel("Total bill [$]")
        rootsstyle.legend()
        assert plt.gcf().number == 1
        plt.savefig(f"{output_dir}/barplot_tips.png")
        plt.close()


def test_barplot_seaborn2():
    diamonds = sns.load_dataset("diamonds")
    diamonds_cut = (
        diamonds.groupby("cut")["price"]
        .count()
        .reset_index()
        .rename(columns={"price": "count"})
    )
    with plt.style.context(rootsstyle.style):
        sns.barplot(
            x="cut",
            y="count",
            data=diamonds_cut,
            order=list(diamonds["cut"].unique())[::-1],
        )
        plt.title("Sparkly Stones")
        rootsstyle.ylabel("Cut")
        plt.ylabel("Count")
        assert plt.gcf().number == 1
        plt.savefig(f"{output_dir}/barplot_sparklystones.png")
        plt.close()


def test_lineplot_seaborn():
    tips = (
        sns.load_dataset("tips")
        .groupby(["day"])["total_bill", "tip"]
        .sum()
        .reset_index()
    )

    with plt.style.context(rootsstyle.style):
        sns.lineplot(x="day", y="total_bill", data=tips, label="total bill")
        sns.lineplot(x="day", y="tip", data=tips, label="tip")
        plt.title("Restaurant income")
        plt.xlabel("Day")
        rootsstyle.ylabel("USD")
        rootsstyle.legend()
        assert plt.gcf().number == 1
        plt.savefig(f"{output_dir}/lineplot.png")
        plt.close()

    
    with plt.style.context(rootsstyle.style):
        sns.lineplot(x="day", y="total_bill", data=tips)
        sns.lineplot(x="day", y="tip", data=tips)
        plt.title("Restaurant income")
        plt.xlabel("Day")
        rootsstyle.ylabel("USD")
        rootsstyle.legend(labels=['total bill', 'tip'])
        assert plt.gcf().number == 1
        plt.savefig(f"{output_dir}/lineplot_2.png")
        plt.close()


def test_violin_plot():
    tips = sns.load_dataset("tips")
    with plt.style.context(rootsstyle.style):
        sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips)
        plt.title("Tip income")
        plt.xlabel("Day")
        rootsstyle.ylabel("USD")
        rootsstyle.legend()
        assert plt.gcf().number == 1
        plt.savefig(f"{output_dir}/violinplot.png")
        plt.close()
