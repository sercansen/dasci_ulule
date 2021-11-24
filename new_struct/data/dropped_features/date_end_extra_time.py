""""""

import pandas as pd
from utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """"""

    pie_feature(data, "date_end_extra_time",
                "Extension de la durée de la campagne")
