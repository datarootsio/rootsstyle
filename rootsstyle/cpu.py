import rootsstyle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__=="__main__":
    df_cpus = pd.read_csv("datasets/cpus.csv")
    with plt.style.context(rootsstyle.style):
        g = sns.lineplot(x='year', y='transistors', data=df_cpus, label='transistors\n[1000s]')
        g = sns.lineplot(x='year', y='watts', data=df_cpus, label='watts')
        g = sns.lineplot(x='year', y='frequency', data=df_cpus, label='frequency\n[MHz]')
        g.set_yscale('log')
        rootsstyle.legend()
        plt.xlabel('Year')
        plt.title("48 Years of Microprocessor Trends")
        plt.savefig(f"images/lineplot_cpus.png")
        plt.close()