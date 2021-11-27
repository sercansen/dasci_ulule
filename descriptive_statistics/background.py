"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, pie_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>background</h5>"

    fig = pie_feature(data, "background",
                      "Présence d'un background dans le projet")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="background", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['background']))
    to_print += "<p>{}</p>".format(
        """Il n'y a pas de corrélation entre la présence d'un background et le succès de la campagne.""")
    return to_print
