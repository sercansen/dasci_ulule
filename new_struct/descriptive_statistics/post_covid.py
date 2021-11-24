"""#TODO"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pdfkit
from scipy.stats import spearmanr
from utils.utils import pie_feature, get_html_from_fig


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""
    string_to_print = """<meta http-equiv="Content-type" content="text/html; charset=utf-8" /><h5>post_covid</h5>"""

    fig = pie_feature(data, "post_covid",
                      "Répartition des projets avant et après Mars 2020.")
    string_to_print += get_html_from_fig(fig)

    fig = plt.figure(edgecolor="b")
    sns.regplot(x="sponsorships_count", y="goal_raised", data=data)
    string_to_print += get_html_from_fig(fig)

    string_to_print += "<p>" + str(spearmanr(data['goal_raised'],
                                             data['sponsorships_count'])) + "</p>"

    string_to_print += """<commentary>L'obtention de sponsors semble être un phénomène très minoritaire. Il ne semble pas y avoir de corrélation entre le succès de la campagne et la présence de sponsors.</commentary>"""
    pdfkit.from_string(string_to_print, './out.pdf',
                       css="./new_struct/styles/styles.css")
