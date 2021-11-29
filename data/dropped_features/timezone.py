"""Ce module concerne tout ce qui touche à la feature "date_end_extra_time"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature date_end_extra_time
"""

from pandas import DataFrame
from matplotlib.pyplot import close
from utils.utils import pie_feature, get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """
    Génère la chaîne de caractère contenant les stats à faire sur une feature.

    Paramètres
    -------- 
    data: DataFrame
        Les données surlesquelles faire les stats

    Valeurs retournées
    -------- 
    string_to_print : str
        La string contenant les stats
    """

    to_print = "<h5>timezone</h5>"
    fig = pie_feature(data, "timezone",
                      "Répartition de la zone temporelle au sein des projets")
    to_print += get_html_from_fig(fig)
    to_print += "<p>L'immense majorité des projets a lieu dans la même zone, la colonne <strong>timezone</strong> est quasiment constante, elle peut être retirée.</p>"
    close(fig)
    return to_print
