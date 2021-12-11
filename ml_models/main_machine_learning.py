from pandas import DataFrame
from preparation_for_ml import prep_data_ml

def machine_learning(cat_name: str, data_general: DataFrame, data_pre_covid: DataFrame, data_post_covid: DataFrame, dict_df: dict) -> str:

    if cat_name == "tout":
        # On utilise les dataframe généraux comme "data_general" et tout le dictionnaire dict_df
        # On prépare les données générales
        X_train, X_test, y_train, y_test = prep_data_ml(data_general)

        #TODO On applique les algos de ML sur les données générales

        #On prépare les données precovid
        X_train, X_test, y_train, y_test = prep_data_ml(data_pre_covid)

        #TODO On applique les algos de ML sur les données pre_covid

        #On prépare les données precovid
        X_train, X_test, y_train, y_test = prep_data_ml(data_post_covid)

        #TODO On applique les algos de ML sur les données post_covid

    else:
        # On utilise les dataframe spéficiques contenus dans dict_df avec les clefs suivante:
        data_cat_general = dict_df["data_" + cat_name]
        data_cat_pre_covid = dict_df["data_pre_covid_" + cat_name]
        data_cat_post_covid = dict_df["data_post_covid_" + cat_name]

        # On prépare les données générales
        X_train, X_test, y_train, y_test = prep_data_ml(data_cat_general)

        #TODO On applique les algos de ML sur les données générales

        #On prépare les données precovid
        X_train, X_test, y_train, y_test = prep_data_ml(data_cat_pre_covid)

        #TODO On applique les algos de ML sur les données pre_covid

        #On prépare les données precovid
        X_train, X_test, y_train, y_test = prep_data_ml(data_cat_post_covid)

        #TODO On applique les algos de ML sur les données post_covid
        
        pass
    return ""
