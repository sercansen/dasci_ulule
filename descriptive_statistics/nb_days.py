"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, plot_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>nb_days</h5>"
    fig = plot_feature(data, "nb_days", "Durée de la campagne de financement",
                       "Identifiant du projet", "Nombre de jours")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="nb_days", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['nb_days']))

    to_print += "<p>{}</p>".format("""Les campagnes semblent durer plus ou moins un mois en grande majorité.
Il ne semble n'y avoir aucune corrélation entre la durée de la campagne et son succès.""")
    return to_print
