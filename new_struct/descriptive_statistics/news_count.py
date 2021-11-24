"""#TODO"""

import seaborn as sns
import pandas as pd
import numpy as np
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    plot_feature(data, "news_count", "Nombre d'actualités postées par projet",
                 "Identifiant du projet", "Nombre d'actualités")

    plot_feature(data, "news_per_days", "Nombre moyen de news par jour de campagne, par projet",
                 "Identifiant du projet", "Nombre de news du projet sur le nombre de jour de campagne")

    plt.figure()
    sns.regplot(x="news_per_days", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['news_per_days'])
    print(markdown.markdown("""Un certain nombre de projets ne donne aucune nouvelle durant la campagne, la grande majorité n'en donne pas plus de cinq durant toute la campagne. La grande majorité des projets ne donne qu'une news tous les dix jours, au mieux.
Il semble y avoir une légère corrélation entre le nombre de news par jour et le succès de la campagne."""))
