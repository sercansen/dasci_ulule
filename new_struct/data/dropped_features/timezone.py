"""Ce module concerne tout ce qui touche à la feature "date_end_extra_time"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature date_end_extra_time
"""

from pandas import DataFrame
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

    fig = pie_feature(data, "timezone",
                      "Répartition de la zone temporelle au sein des projets")
    return get_html_from_fig(fig)
