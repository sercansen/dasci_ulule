"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, plot_feature_log


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>goal</h5>"
    fig = plot_feature_log(data, "goal", "Objectif de validation du projet",
                           "Identifiant du projet", "Objectif euros")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="goal", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['goal']))
    to_print += "<p>{}</p>".format("""La majorité des projets semble se concentrer autour de la même fourchette de valeur, malgré quelques valeurs extrêmes.
Il ne semble pas y avoir de corrélation entre le montant de succès de la campagne et son succès.""")
    return to_print
