"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import pie_feature, get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """#TODO"""
    to_print = """<h5>post_covid</h5>"""

    fig = pie_feature(data, "post_covid",
                      "Répartition des projets avant et après Mars 2020 (après=True)")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure(edgecolor="b")
    sns.regplot(x="post_covid", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>" + str(spearmanr(data['goal_raised'],
                                      data['post_covid'])) + "</p>"

    to_print += """<p>L'obtention de sponsors semble être un phénomène très minoritaire. Il ne semble pas y avoir de corrélation entre le succès de la campagne et la présence de sponsors.</p>"""
    return to_print
