import random
import itertools
import rootsstyle
import pandas as pd
import seaborn as sns
from rootsstyle import colors
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = "images"

def test_palette():
    color_values = list(colors.values())
    nb_colors = len(color_values)
    plt.figure(figsize=(8, 8))
    ax = plt.gca()

    #Plot ordered palette
    ax.set_ylim(0, 6)
    ax.set_xlim(0, nb_colors)
    for i in range(nb_colors):
        ax.add_patch(patches.Rectangle((i,5.05), width=1, height=0.92, linewidth=0, facecolor=color_values[i]))

    #Plot random spots next to each other
    for x, y in itertools.product(list(range(nb_colors)), list(range(5))):
        color = color_values[random.randint(0, nb_colors-1)]
        height = 0.92 if y==4 else 1
        ax.add_patch(patches.Rectangle((x,y), width=1, height=height, linewidth=0, facecolor=color))
    
    plt.axis('off')
    plt.savefig(f"{OUTPUT_DIR}/palette.png", transparent=True)
    plt.close()

def test_scatterplot():
    df_penguins = sns.load_dataset("penguins")
    with plt.style.context(rootsstyle.style):
        sns.scatterplot(x='body_mass_g', y='flipper_length_mm', marker='+', data=df_penguins, hue='species')
        rootsstyle.legend()
        rootsstyle.ylabel('flipper length\n[mm]')
        plt.xlabel('body mass [g]')
        plt.title("Penguins")
        plt.savefig(f"{OUTPUT_DIR}/scatterplot.png")
        plt.close()

def test_lineplot():
    df_flights = sns.load_dataset("flights")
    with plt.style.context(rootsstyle.style):
        sns.lineplot(x='month', y='passengers', data=df_flights, hue='year', palette=rootsstyle.palettes['dataroots-green'][:12])
        rootsstyle.legend()
        rootsstyle.ylabel('passengers')
        plt.xlabel('month')
        plt.title("Flights")
        plt.savefig(f"{OUTPUT_DIR}/lineplot_green.png")
        plt.close()


        sns.lineplot(x='month', y='passengers', data=df_flights, hue='year', palette=rootsstyle.palettes['dataroots-blue'][:12])
        rootsstyle.legend()
        rootsstyle.ylabel('passengers')
        plt.xlabel('month')
        plt.title("Flights")
        plt.savefig(f"{OUTPUT_DIR}/lineplot_blue.png")
        plt.close()
    
    df_cars = sns.load_dataset("mpg")
    df_usa = df_cars[df_cars['origin']=='usa'].groupby('model_year').mean().reset_index()
    df_japan = df_cars[df_cars['origin']=='japan'].groupby('model_year').mean().reset_index()
    df_europe = df_cars[df_cars['origin']=='europe'].groupby('model_year').mean().reset_index()
    with plt.style.context(rootsstyle.style):
        sns.lineplot(x='model_year', y='mpg', data=df_usa, label='USA')
        sns.lineplot(x='model_year', y='mpg', data=df_japan, label='Japan')
        sns.lineplot(x='model_year', y='mpg', data=df_europe, label='Europe')
        rootsstyle.legend()
        rootsstyle.ylabel('mpg')
        plt.xlabel('model year')
        plt.title("Cars")
        plt.savefig(f"{OUTPUT_DIR}/lineplot_cars.png")
        plt.close()


def test_barplot():
    df_penguins = sns.load_dataset("penguins")
    df_penguins = df_penguins.groupby(["island", "species"]).size().to_frame('count').reset_index()
    with plt.style.context(rootsstyle.style):
        sns.barplot(x='island', y='count',data=df_penguins, hue='species')
        rootsstyle.ylabel('Penguins')
        plt.xlabel('Island')
        rootsstyle.legend()
        plt.savefig(f"{OUTPUT_DIR}/barplot.png")
        plt.close()

def test_violinplot():
    df_tips = sns.load_dataset("tips")
    with plt.style.context(rootsstyle.style):
        sns.violinplot(x="day", y="total_bill", hue="smoker", data=df_tips)
        plt.title("Tip income")
        plt.xlabel("Day")
        rootsstyle.ylabel("USD")
        rootsstyle.legend()
        plt.savefig(f"{OUTPUT_DIR}/violinplot.png")
        plt.close()

def test_pieplot():
    df_penguins = sns.load_dataset("penguins")
    df_penguins = df_penguins.groupby("species").size().to_frame('count').reset_index()
    with plt.style.context(rootsstyle.style):
        plt.pie(df_penguins['count'], labels=df_penguins['species'], autopct='%.0f%%')
        plt.title("Pinguin distribution")
        rootsstyle.legend()
        plt.savefig(f"{OUTPUT_DIR}/pieplot.png")
        plt.close()