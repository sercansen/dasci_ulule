"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from pandas import DataFrame
from utils.utils import get_html_from_fig, pie_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""
    to_print = "<h5>sponsorships_count</h5>"
    fig = pie_feature(data, "sponsorships_count",
                      "Représentation du nombre de sponsors parmi les projets.")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="sponsorships_count", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['sponsorships_count']))
    to_print += "<p>{}</p>".format("""L'obtention de sponsors semble être un phénomène très minoritaire.
Il ne semble pas y avoir de corrélation entre le succès de la campagne et la présence de sponsors.""")
    return to_print
