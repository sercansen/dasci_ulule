"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, plot_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>news_count</h5>"
    fig = plot_feature(data, "news_count", "Nombre d'actualités postées par projet",
                       "Identifiant du projet", "Nombre d'actualités")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plot_feature(data, "news_per_days", "Nombre moyen de news par jour de campagne, par projet",
                       "Identifiant du projet", "Nombre de news du projet sur le nombre de jour de campagne")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="news_per_days", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['news_per_days']))
    to_print += "<p>{}</p>".format("""Un certain nombre de projets ne donne aucune nouvelle durant la campagne, la grande majorité n'en donne pas plus de cinq durant toute la campagne. La grande majorité des projets ne donne qu'une news tous les dix jours, au mieux.
Il semble y avoir une légère corrélation entre le nombre de news par jour et le succès de la campagne.""")
    return to_print
