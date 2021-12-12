from pandas import DataFrame
from ml_models import mlp
from ml_models.preparation_for_ml import prep_data_ml


def machine_learning(cat_name: str, data_general: DataFrame, data_pre_covid: DataFrame, data_post_covid: DataFrame, dict_df: dict) -> str:

    to_print = """"""
    if cat_name == "tout":
        # On utilise les dataframe généraux comme "data_general" et tout le dictionnaire dict_df

        # INSERER ML ICI
        pass

    else:
        # On utilise les dataframe spéficiques contenus dans dict_df avec les clefs suivante:
        data_cat_general = dict_df["data_" + cat_name]
        data_cat_pre_covid = dict_df["data_pre_covid_" + cat_name]
        data_cat_post_covid = dict_df["data_post_covid_" + cat_name]

        # INSERER ML ICI

    to_print += "<h2>Application d'un Multi Layer Perceptron</h2>"
    to_print += mlp.mlp(data_general)

    return to_print
