"""Ce module concerne tout ce qui touche à la feature "date_end_extra_time"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature date_end_extra_time
"""

from matplotlib.pyplot import close
from pandas import DataFrame
from utils.utils import pie_feature, get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """
    Génère la chaîne de caractère contenant les stats à faire sur une feature

    Paramètres
    -------- 
    data: DataFrame
        Les données surlesquelles faire les stats

    Valeurs retournées
    -------- 
    string_to_print : str
        La string contenant les stats
    """

    to_print = """<h5>date_end_extra_time</h5>"""
    fig = pie_feature(data, "date_end_extra_time",
                      "Extension de la durée de la campagne")
    to_print += get_html_from_fig(fig)
    close(fig)
    to_print += "<p>La colonne date_end_extra_time sera retirée car aucun projet ayant échoué n'y a fait appel et c'est un phénomène très minoritaire.</p>"
    return to_print
