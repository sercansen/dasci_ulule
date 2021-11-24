""""""

import pandas as pd
from utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """"""

    pie_feature(data, "timezone",
                "Répartition de la zone temporelle au sein des projets")
