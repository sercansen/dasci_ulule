"""#TODO"""

from matplotlib.pyplot import close
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, pie_feature


def show_stats(data: DataFrame) -> str:
    """#TODO"""
    to_print = "<h5>payment_methods</h5>"
    fig = pie_feature(data, "payment_methods",
                      "Représentation des moyens de paiement autorisés par les projets")
    to_print += get_html_from_fig(fig)
    close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['payment_methods']))

    to_print += "<p>{}</p>".format("""La totalité autorise le trio "card, creditcard, saving" et 75% l'utilisent.
Il ne semble y avoir aucune corrélation entre le moyen de paiement et le succès de la campagne.""")
    return to_print
