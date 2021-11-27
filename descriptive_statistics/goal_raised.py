"""#TODO"""

from matplotlib.pyplot import close
from pandas import DataFrame
from utils.utils import pie_feature, get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """#TODO"""
    to_print = "<h5>goal_raised</h5>"
    fig = pie_feature(data, "goal_raised",
                      "Représentation du taux de succès des projets, succès=True")
    to_print += get_html_from_fig(fig)
    close(fig)
    to_print += "<p>{}</p>".format(
        """Pour rappel, le taux de succès des projets de la plateforme en 2021 est de 79%.""")
    return to_print
