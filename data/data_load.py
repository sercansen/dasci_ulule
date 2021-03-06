"""
Charge les données contenues dans des fichiers .CSV

Fonctions
----------
load_data
    Charge les données depuis le CSV contenant toutes les données (très lourd)
load_clean_data
    Charge les données depuis le CSV contenant les données nettoyées
load_pre_covid_data
    Charge les données nettoyées et pré-covid
load_post_covid_data
    Charge les données nettoyées et post-covid
load_categorical_data
    Charge les données pour une catégorie
_update_data_frame
    Retransforme les chaînes de caractères en dictionnaires
"""

import ast
from pandas import read_csv, DataFrame


def load_data() -> DataFrame:
    """
    Charge les données depuis le CSV contenant toutes les données (très lourd)

    Valeurs retournées
    -------- 
    df : DataFrame
        Les données chargées.
    """

    df = read_csv("./data/ulule_data.csv", low_memory=False)
    print("-- Fin de la lecture des données")
    return df


def load_clean_data() -> DataFrame:
    """
    Charge les données depuis le CSV contenant les données nettoyées.

    La fonction retransforme les données comme les chaînes de caractère
    en dictionnaires.

    Valeurs retournées
    -------- 
    df : DataFrame
        Les données chargées.
    """

    df = read_csv("./data/clean_data.csv")
    return df


def load_pre_covid_data() -> DataFrame:
    """
    Charge les données pré-covid nettoyées depuis un CSV.

    La fonction retransforme les données comme les chaînes de caractère
    en dictionnaires.

    Valeurs retournées
    -------- 
    df : DataFrame
        Les données chargées.
    """

    df = read_csv("./data/clean_data_pre_covid.csv")
    return df


def load_post_covid_data() -> DataFrame:
    """
    Charge les données post-covid nettoyées depuis un CSV.

    La fonction retransforme les données comme les chaînes de caractère
    en dictionnaires.

    Valeurs retournées
    -------- 
    df : DataFrame
        Les données chargées.
    """
    df = read_csv("./data/clean_data_post_covid.csv")
    return df


def load_categorical_data(file_name) -> DataFrame:
    """
    Charge les données depuis le CSV contenant une donnée catégorielle.

    La fonction retransforme les données comme les chaînes de caractère
    en dictionnaires.

    Valeurs retournées
    -------- 
    df : DataFrame
        Les données chargées.
    """

    df = read_csv(file_name)
    return df


