"""Ce module concerne tout ce qui touche à la feature "lowest_contribution_amount"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature lowest_contribution_amount
"""

from pandas import DataFrame
from matplotlib.pyplot import close
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

    to_print = "<h5>lowest_contribution_amount</h5>"
    fig = pie_feature(data, "lowest_contribution_amount",
                      "Répartition de la contribution minimale au sein des projets")
    to_print += get_html_from_fig(fig)
    close(fig)
    to_print += "<p>Etant quasiment constante, la colonne <strong>lowest_contribution_amount</strong> peut également être retirée car non pertinente.</p>"
    return to_print
