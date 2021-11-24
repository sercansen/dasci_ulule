""""""

import pandas as pd
from utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """"""

    pie_feature(data, "comments_enabled",
                "Répartition des permissions de commentaires")
