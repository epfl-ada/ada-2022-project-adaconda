from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def plot_comparison(df):
    top_5_categories = list(df.groupby("categories").max().sort_values("nb_videos", ascending=False).reset_index().categories.head(5)) + ["Sports"]

    fig = plt.figure(figsize=(15, 8))
    ax = fig.add_subplot(111)
    tmp = df.copy()
    tmp["date"] = tmp["date"].dt.strftime("%b %Y")
    palette = {category: "grey" for category in tmp[~tmp["categories"].isin(top_5_categories)].categories}

    sns.lineplot(x="date", y="nb_videos", hue="categories", data=tmp[tmp["categories"].isin(top_5_categories)])
    sns.lineplot(x="date", y="nb_videos", hue="categories", palette=palette, data=tmp[~tmp["categories"].isin(top_5_categories)])

    start, end = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(start, end, 6))
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Number of Videos posted")
    plt.show()
