"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, plot_feature


def show_stats(data: DataFrame) -> None:
    """#TODO"""

    to_print = "<h5>nb_rewards</h5>"
    fig = plot_feature(data, "nb_rewards", "", "", "")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="nb_rewards", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['nb_rewards']))
    to_print += "<p>{}</p>".format("""Une majorité de projets a entre 0 et 50 tiers de rewards. Les projets réussis ont une moyenne de nombre de tiers légèrement plus élevée que les projets ratés, mais cela ne semble pas réellement discriminer entre succès et échec d'un projet.""")

    to_print += "<p>{}</p>".format("""???""")
    return to_print
