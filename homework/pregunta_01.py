"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import matplotlib.pyplot as plt
    import pandas as pd

    data = pd.read_csv("files/input/news.csv", index_col=0)

    fig, ax = plt.subplots(figsize=(8, 6))

    colors = {
        "Television": "#6d6d6d",
        "Newspaper": "#8c8c8c",
        "Radio": "#cfcfcf",
        "Internet": "#2b7bb9",
    }

    for series in ["Television", "Newspaper", "Radio"]:
        ax.plot(data.index, data[series], color=colors[series], linewidth=2)

    ax.plot(data.index, data["Internet"], color=colors["Internet"], linewidth=3)

    first_year = data.index[0]
    last_year = data.index[-1]

    for series in ["Television", "Newspaper", "Radio", "Internet"]:
        ax.scatter(first_year, data.loc[first_year, series], color=colors[series], s=40, zorder=3)
        ax.scatter(last_year, data.loc[last_year, series], color=colors[series], s=40, zorder=3)

    ax.set_title("How people get their news", fontsize=22, pad=18)
    ax.text(
        0.5,
        0.96,
        "An increasing proportion cite the internet as their primary news source",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=10,
    )

    ax.set_xlim(first_year - 0.6, last_year + 0.6)
    ax.set_ylim(10, 85)
    ax.set_xticks(data.index)
    ax.set_yticks([])

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    ax.spines["bottom"].set_color("black")
    ax.tick_params(axis="x", labelsize=12)

    ax.text(
        first_year - 0.2,
        data.loc[first_year, "Television"],
        f"Television {data.loc[first_year, 'Television']}%",
        ha="right",
        va="center",
        fontsize=14,
        color=colors["Television"],
    )
    ax.text(
        first_year - 0.2,
        data.loc[first_year, "Newspaper"],
        f"Newspaper {data.loc[first_year, 'Newspaper']}%",
        ha="right",
        va="center",
        fontsize=14,
        color=colors["Newspaper"],
    )
    ax.text(
        first_year - 0.2,
        data.loc[first_year, "Radio"],
        f"Radio {data.loc[first_year, 'Radio']}%",
        ha="right",
        va="center",
        fontsize=14,
        color=colors["Radio"],
    )
    ax.text(
        first_year - 0.2,
        data.loc[first_year, "Internet"],
        f"Internet {data.loc[first_year, 'Internet']}%",
        ha="right",
        va="center",
        fontsize=14,
        color=colors["Internet"],
    )

    ax.text(
        last_year + 0.25,
        data.loc[last_year, "Television"],
        f"{data.loc[last_year, 'Television']}%",
        ha="left",
        va="center",
        fontsize=14,
        color=colors["Television"],
    )
    ax.text(
        last_year + 0.25,
        data.loc[last_year, "Newspaper"],
        f"{data.loc[last_year, 'Newspaper']}%",
        ha="left",
        va="center",
        fontsize=14,
        color=colors["Newspaper"],
    )
    ax.text(
        last_year + 0.25,
        data.loc[last_year, "Radio"],
        f"{data.loc[last_year, 'Radio']}%",
        ha="left",
        va="center",
        fontsize=14,
        color=colors["Radio"],
    )
    ax.text(
        last_year + 0.25,
        data.loc[last_year, "Internet"],
        f"{data.loc[last_year, 'Internet']}%",
        ha="left",
        va="center",
        fontsize=14,
        color=colors["Internet"],
    )

    output_dir = "files/plots"
    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(os.path.join(output_dir, "news.png"), bbox_inches="tight")
    plt.close(fig)