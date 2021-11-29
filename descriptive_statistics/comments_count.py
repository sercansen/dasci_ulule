"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, plot_feature_log


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_string = "<h5>comments_count</h5>"
    fig = plot_feature_log(data, "comments_count", "Nombre de commentaires par projet",
                           "Identifiant du projet", "Nombres de commentaires")
    to_string += "<p>{}</p>".format(get_html_from_fig(fig))
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="comments_count", y="goal_raised", data=data)
    to_string += "<p>{}</p>".format(get_html_from_fig(fig))
    plt.close(fig)

    to_string += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['comments_count']))
    to_string += "<p>{}</p>".format("""Les projets reçoivent globalement assez peu de commentaires. La plupart des projets qui ont beaucoup de commentaires, ont bien fonctionné.
Il semble y avoir une petite corrélation entre le nombre de commentaires et le succès de la campagne.""")
    return to_string
