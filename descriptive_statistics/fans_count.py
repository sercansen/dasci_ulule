"""#TODO"""

from pandas.io.parquet import to_parquet
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import plot_feature, get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """#TODO"""
    to_print = "<h5>fans_count</h5>"
    fig = plot_feature(data, "fans_count",
                       "Représentation du nombre de fans", "Id du projet", "Nombre de fans")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="fans_count", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['fans_count']))

    to_print += "<p>{}</p>".format("""La présence de fans semble être un phénomène très minoritaire, il serait intéressant de vérifier si les projets suivis ont été plus réussis que les autres.
Il est possible de conclure quand à l'existence d'une corrélation entre le succès de la campagne et le nombre de fans.""")
    return to_print
