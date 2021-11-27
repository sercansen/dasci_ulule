"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, plot_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>supporters_count</h5>"
    fig = plot_feature(data, "supporters_count", "Nombre de supporters par projet",
                       "Identifiant du projet", "Nombre de supporters")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    sns.regplot(x="supporters_count", y="goal_raised", data=data, ax=ax1)
    f.suptitle("Succès du projet en fonction du nombre de supporters")
    ax2.set_xlabel("Nombre de supporters")
    ax2.set_ylabel("Succès du projet, 1=succès")
    ax2.plot(data.supporters_count, data.goal_raised, "+")
    to_print += get_html_from_fig(f)
    plt.close(f)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['supporters_count']))
    to_print += "<p>{}</p>".format(
        """On constate une bonne corrélation entre le succès du projet et le nombre de supporters.""")
    return to_print
