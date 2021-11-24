"""#TODO"""

import pandas as pd
import markdown
from scipy.stats import spearmanr
from new_struct.utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""
    pie_feature(data, "goal_raised",
                "Représentation du taux de succès des projets, succès=True")

    print(markdown.markdown(
        """Pour rappel, le taux de succès des projets de la plateforme en 2021 est de 79%."""))
