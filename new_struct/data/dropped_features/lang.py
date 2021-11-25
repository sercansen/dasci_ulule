"""Ce module concerne tout ce qui touche à la feature "lang"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature lang
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

    fig = pie_feature(
        data, "lang", "Répartition des langues au sein des projets")
    return get_html_from_fig(fig)
