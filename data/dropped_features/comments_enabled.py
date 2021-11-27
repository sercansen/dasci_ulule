"""Ce module concerne tout ce qui touche à la feature "comments_enabled"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature comments_enabled
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

    to_print = "<h5>comments_enabled</h5>"
    fig = pie_feature(data, "comments_enabled",
                      "Répartition des permissions de commentaires")
    to_print += get_html_from_fig(fig)
    close(fig)
    to_print += "<p>Une écrasante majorité des projets autorise les commentaires pour tous les utilisateurs, la colonne <strong>comments_enabled</strong> n'est donc pas pertinente.</p>"
    return to_print
