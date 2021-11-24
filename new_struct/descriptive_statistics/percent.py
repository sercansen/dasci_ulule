"""#TODO"""

import pandas as pd
import markdown
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature_log


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    plot_feature_log(data, "percent", "Pourcentage du montant de succès demandé effectivement atteint par projet",
                     "Identifiant du projet", "Pourcentage atteint")
    print(markdown.markdown("""On note trois catégories de projets : 
- ceux qui échouent complétement (moins de 50% du montant demandé sont atteints)
- ceux qui réussissent "normalement" (entre 100% et 175% du montant demandé sont atteints)
- ceux qui réussissent "fortement" (au-delà de 200%)"""))
