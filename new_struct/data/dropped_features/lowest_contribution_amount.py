""""""

import pandas as pd
from utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """"""

    pie_feature(data, "lowest_contribution_amount",
                "Répartition de la contribution minimale au sein des projets")
