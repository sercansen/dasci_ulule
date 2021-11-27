u"""#TODO"""

from matplotlib.pyplot import close
from pandas import DataFrame
from utils.utils import plot_feature_log, get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>percent</h5>"
    fig = plot_feature_log(data, "percent", "Pourcentage du montant de succès demandé effectivement atteint par projet",
                           "Identifiant du projet", "Pourcentage atteint")
    to_print += get_html_from_fig(fig)
    close(fig)

    to_print += "<p>{}</p>".format("On note trois catégories de projets :")
    to_print += "<ul>{}</ul>".format("""
<li>ceux qui échouent complétement (moins de 50% \du montant demandé sont atteints)</li>
<li>ceux qui réussissent "normalement" (entre 100% \et 175% \du montant demandé sont atteints)</li>
<li>ceux qui réussissent "fortement" (au-delà de 200%)</li></ul>""")
    return to_print
