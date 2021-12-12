from pandas import DataFrame
from ml_models.prep_stat import prep_data_ml, confusion_matrix, roc_curve
from ml_models.model_building import log_reg

import matplotlib.pyplot as plt

def machine_learning(cat_name: str, data_general: DataFrame, data_pre_covid: DataFrame, data_post_covid: DataFrame, dict_df: dict) -> str:

    to_print = "<h2>Tuning et performance des différents modèles</h2>"

    if cat_name == "tout":
        # On utilise les dataframe généraux comme "data_general" et tout le dictionnaire dict_df
        # On prépare les données générales
        data_general = data_general.set_index('Unnamed: 0')
        X_train, X_test, y_train, y_test = prep_data_ml(data_general)

        #TODO On applique les algos de ML sur les données générales
        to_print += "<h3>Régression logistique</h3>"
        log_reg_model, log_reg_preds, txt = log_reg(X_train, X_test, y_train, y_test)
        to_print += txt
        to_print += confusion_matrix(y_test, log_reg_preds)
        to_print += roc_curve(X_test, y_test, log_reg_model)

        #On prépare les données precovid
        data_pre_covid = data_pre_covid.set_index('Unnamed: 0')
        X_train, X_test, y_train, y_test = prep_data_ml(data_pre_covid)

        #TODO On applique les algos de ML sur les données pre_covid

        #On prépare les données precovid
        data_post_covid = data_post_covid.set_index('Unnamed: 0')
        X_train, X_test, y_train, y_test = prep_data_ml(data_post_covid)

        #TODO On applique les algos de ML sur les données post_covid

    else:
        # On utilise les dataframe spéficiques contenus dans dict_df avec les clefs suivante:
        data_cat_general = dict_df["data_" + cat_name]
        data_cat_pre_covid = dict_df["data_pre_covid_" + cat_name]
        data_cat_post_covid = dict_df["data_post_covid_" + cat_name]

        # On prépare les données générales
        data_cat_general = data_cat_general.set_index('Unnamed: 0')
        X_train, X_test, y_train, y_test = prep_data_ml(data_cat_general)

        #TODO On applique les algos de ML sur les données générales

        #On prépare les données precovid
        data_cat_pre_covid = data_cat_pre_covid.set_index('Unnamed: 0')
        X_train, X_test, y_train, y_test = prep_data_ml(data_cat_pre_covid)

        #TODO On applique les algos de ML sur les données pre_covid

        #On prépare les données precovid
        data_cat_post_covid = data_cat_post_covid.set_index('Unnamed: 0')
        X_train, X_test, y_train, y_test = prep_data_ml(data_cat_post_covid)

        #TODO On applique les algos de ML sur les données post_covid
        
        pass
    return to_print
