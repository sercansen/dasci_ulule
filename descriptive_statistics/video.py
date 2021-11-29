"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from pandas import DataFrame
from utils.utils import get_html_from_fig, pie_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>video</h5>"
    fig = pie_feature(data, "video", "Présence d'une vidéo dans le projet")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="video", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['video']))
    to_print += "<p>{}</p>".format(
        """Il ne semble pas y avoir de corrélation entre le fait de posséder une vidéo et le succès de la campagne""")
    return to_print
