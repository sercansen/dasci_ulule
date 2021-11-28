"""#TODO"""

import ast
from pandas import read_csv, DataFrame


def load_data() -> DataFrame:
    """#TODO """
    df = read_csv("./data/ulule_data.csv", low_memory=False)
    print("-- Fin de la lecture des données")
    return df


def load_clean_data() -> DataFrame:
    """#TODO """
    return _update_data_frame(read_csv("./data/clean_data.csv"))


def load_pre_covid_data() -> DataFrame:
    """#TODO """
    return _update_data_frame(read_csv("./data/clean_data_pre_covid.csv"))


def load_post_covid_data() -> DataFrame:
    """#TODO """
    return _update_data_frame(read_csv("./data/clean_data_post_covid.csv"))


def _update_data_frame(data_frame: DataFrame) -> None:
    def update_col_main_tag(x):
        if type(x["main_tag"]) == str:
            return ast.literal_eval(x["main_tag"])
    data_frame["main_tag"] = data_frame.apply(update_col_main_tag, axis=1)
