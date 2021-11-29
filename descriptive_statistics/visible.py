"""#TODO"""

import seaborn as sns
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from pandas import DataFrame
from utils.utils import get_html_from_fig, pie_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>visible</h5>"
    fig = pie_feature(data, "visible",
                      "Indexation sur les moteurs de recherches du projet")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    sns.regplot(x="visible", y="goal_raised", data=data, ax=ax1)
    f.suptitle("Succès du projet en fonction de sa visibilité")
    ax2.set_xlabel("Visibilité")
    ax2.set_ylabel("Succès du projet, 1=succès")
    ax2.plot(data.visible, data.goal_raised, "+")
    to_print += get_html_from_fig(f)
    plt.close(f)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['visible']))
    to_print += "<p>{}</p>".format("""La plupart des projets sont indexés sur les moteurs de recherches.
On ne constate cepandant pas de corrélation entre la visibilité et le succès d'un projet""")
    return to_print
