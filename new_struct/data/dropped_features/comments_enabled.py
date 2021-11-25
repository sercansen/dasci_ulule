"""Ce module concerne tout ce qui touche à la feature "comments_enabled"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature comments_enabled
"""

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

    fig = pie_feature(data, "comments_enabled",
                      "Répartition des permissions de commentaires")
    return get_html_from_fig(fig)
