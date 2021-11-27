"""Ce module concerne tout ce qui touche à la feature "lang"

Fonctions
----------
show_stats
    Affiche les statistiques faites avec la feature lang
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

    to_print = "<h5>lang</h5>"

    fig = pie_feature(
        data, "lang", "Répartition des langues au sein des projets")
    to_print += get_html_from_fig(fig)
    close(fig)
    to_print += """<p>Les autres langues que le français étant très minoritaires, on peut retirer tous les projets concernés ainsi que les colonnes suivantes :</p>
        <ul>
            <li><strong>description_[Langue!=fr]</strong></li>
            <li><strong>description_funding_[Langue!=fr]</strong></li>
            <li><strong>lang</strong></li>
            <li><strong>name_[Langue!=fr]</strong></li>
            <li><strong>subtitle_[Langue!=fr]</strong></li>
        </ul>"""
    return to_print
