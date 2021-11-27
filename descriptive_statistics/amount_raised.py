"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import plot_feature_log, get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """#TODO"""
    to_print = """"""
    fig = plot_feature_log(data, "amount_raised", "Montant levé par projet",
                           "Identifiant du projet", "Montant levé en euros")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="amount_raised", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['amount_raised']))

    to_print += "<p>{}</p>".format("""Les projets semblent assez homogènes dans les montants levés même si moins nombreux pour les plus hauts montants.
Il semble y avoir une bonne corrélation entre le montant obtenu et le succès de la campagne (peu surprenant).""")
    return to_print
