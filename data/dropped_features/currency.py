"""Ce module concerne tout ce qui touche à la feature "currency"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature currency
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

    to_print = "<h5>currency</h5>"
    fig = pie_feature(data,
                      "currency", "Répartition de la monnaie utilisée au sein des projets")
    to_print += get_html_from_fig(fig)
    close(fig)
    to_print += "<p>L'écrasante majorité des projets est en euro, il est donc possible de retirer la colonne <strong>currency</strong> ainsi que la colonne <strong>currency_display</strong>, sans oublier les projets concernés.</p>"
    return to_print
