"""
Préparation des données : retrait des lignes et colonnes inutiles ciblées.

Fonctions
----------
prepare_data
    Retire les lignes et colonnes inutiles, transforme les variables etc.
generate_clean_data
    Exporte les données traitées au format .CSV
"""


import numpy as np
import ast
import os
from typing import Tuple
from pandas import DataFrame
from datetime import datetime
from data.data_understanding import understand_data
from bs4 import BeautifulSoup


def prepare_data(display_explanations: bool = False) -> Tuple[DataFrame, DataFrame, DataFrame, str]:
    """
    Prépare les données pour l'étude à venir.

    Retire les colonnes inutiles, les projets ne répondant pas à certains
    critères (ne pas avoir de case vide dans certaines colonnes, ...) ou
    transforme certaines colonnes.

    Paramètres
    -------- 
    display_explanations : bool, optionnel
        Détermine s'il faut afficher les explications sur ce qui est fait
        (utile en cas de débuggage).

    Valeurs retournées
    -------- 
    data : DataFrame
        Les données nettoyées.
    data_pre_covid : DataFrame
        Les données nettoyées concernant les projets pré-covid.
    data_post_covid : DataFrame
        Les données nettoyées concernant les projets post-covid.
    string_to_print : str
        La chaîne de caractère contenant les affichages.
    """

    data, string_to_print = understand_data(
        display_explanations=display_explanations)

    # Retrait de lignes inutiles
    unfinished_projets = data[~data.finished]
    data.drop(unfinished_projets.index, inplace=True)

    cancelled_projects = data[data.is_cancelled]
    data.drop(cancelled_projects.index, inplace=True)

    foreign_language_projects = data[data.lang != "fr"]
    data.drop(foreign_language_projects.index, inplace=True)

    not_euro_project = data[data.currency != "EUR"]
    data.drop(not_euro_project.index, inplace=True)

    foreign_country_project = data[data.country != "FR"]
    data.drop(foreign_country_project.index, inplace=True)

    # Retrait de colonnes inutiles
    data.drop(columns=['absolute_url',
                       'address_required',
                       'phone_number_required',
                       'comments_enabled',
                       'committed',
                       'country',
                       'currency',
                       'currency_display',
                       'date_end_extra_time',
                       'delivery',
                       'description_ca',
                       'description_de',
                       'description_en',
                       'description_es',
                       'description_it',
                       'description_nl',
                       'description_pt',
                       'description_funding_ca',
                       'description_funding_de',
                       'description_funding_en',
                       'description_funding_es',
                       'description_funding_it',
                       'description_funding_nl',
                       'description_funding_pt',
                       'description_yourself_ca',
                       'description_yourself_de',
                       'description_yourself_en',
                       'description_yourself_es',
                       'description_yourself_it',
                       'description_yourself_nl',
                       'description_yourself_pt',
                       'discussions_thread_id',
                       'image',
                       'is_cancelled',
                       'is_in_extra_time',
                       'finished',
                       'lang',
                       'location',
                       'lowest_contribution_amount',
                       'main_image',
                       'name_ca',
                       'name_de',
                       'name_en',
                       'name_es',
                       'name_it',
                       'name_nl',
                       'name_pt',
                       'orders_count',
                       'owner',
                       'required_personal_id_number',
                       'resource_uri',
                       'sharing_urls',
                       'slug',
                       'subtitle_ca',
                       'subtitle_de',
                       'subtitle_en',
                       'subtitle_es',
                       'subtitle_it',
                       'subtitle_nl',
                       'subtitle_pt',
                       'time_left',
                       'time_left_short',
                       'timezone',
                       'urls',
                       'user_role'], inplace=True)

    if display_explanations:
        summary = """<h3>Bilan : colonnes restantes</h3>
        <p>Les colonnes suivantes sont conservées dans le dataset, mais peuvent nécessiter un travail supplémentaire, comme la colonne <strong>video</strong>. Nous n'allons en effet pas étudier la vidéo du projet en elle même mais plutôt le fait qu'elle existe ou non par exemple.</p>

        <p>Le set contient une trentaine de colonnes pour environs 40.000 projets.</p>"""
        string_to_print += summary
        string_to_print += "<p>{}</p>".format(str(data.columns))

    # Transformations de données
    # Binarisation
    summary_transformation = """<p>Certaines colonnes doivent être binarisée pour représenter ou non la présence d'un objet (comme une vidéo). Binarisation de <strong>video</strong> et <strong>background</strong></p>"""
    if display_explanations:
        string_to_print += summary_transformation

    def binarize(x):
        return 1 if type(x) == str else 0

    data.background = data.background.apply(binarize)
    data.video = data.video.apply(binarize)

    # Rewards
    if display_explanations:
        rewards = """<h5>rewards</h5><p>Pour chaque projet, l'attribut reward propose un certain nombre de rewards dans une liste. Pour chaque reward, plusieurs informations sont disponibles, comme une date de livraison, un nombre de stock etc. Il est possible pour une reward d'avoir plusieurs variantes, par exemple une couleur pour un T-shirt, localisé dans l'attribut 'variants'.</p>

        <p>Les stocks seront toujours nuls (les projets sont finis) mais il est possible de savoir combien de chacune des rewards ont été prises, et à quel prix. Il est donc possible de voir, pour un projet, ce qui a été le plus rentable i.e. plein de petites rewards ou peu de grosses; et de croiser avec tous les autres projets.</p>

        <p>La colonne doit donc être retravaillée pour extraire une liste de dictionnaires par projet.</p>"""
        string_to_print += rewards

    def recup_in_str_rewards(x):
        allowed_keys = ["description_fr", "id",
                        "price", "stock_taken", "variants"]
        allowed_keys_variants = [
            "description_fr", "id", "price", "stock_taken"]
        rewards_dict_list = ast.literal_eval(x["rewards"])
        for dictionnary in rewards_dict_list:
            if "variants" in dictionnary:
                dictionnary["variants"] = [{key: val for key, val in variant.items(
                ) if key in allowed_keys_variants} for variant in dictionnary["variants"]]

        return [{key: val for key, val in dictionnary.items() if key in allowed_keys} for dictionnary in rewards_dict_list]

    data['rewards'] = data.apply(recup_in_str_rewards, axis=1)

    # Main_tag
    if display_explanations:
        main_tag = """<h5>main_tag</h5>
<p>Dans la mesure où les projets ne se comportent pas de la même façon selon leur type, il peut être intéressant d'étudier les tags utilisés pour les décrire. Seuls nous intéressent l'id et le nom en français du tag, il faut donc les extraire.</p>"""
        string_to_print += main_tag

    def recup_in_str_main_tag(x):
        if type(x["main_tag"]) == str:
            return {key: val for key, val in ast.literal_eval(x["main_tag"]).items() if key == 'name_fr' or key == 'id'}

    data["main_tag"] = data.apply(recup_in_str_main_tag, axis=1)

    # Retrait de lignes incomplètes
    essentials_columns_names = ['date_start', 'date_end', 'amount_raised', 'comments_count', 'date_start', 'date_end', 'description_fr',
                                'description_funding_fr', 'description_yourself_fr', 'fans_count',
                                'goal', 'goal_raised', 'id', 'main_tag', 'name_fr', 'news_count', 'percent',
                                'rewards', 'sponsorships_count', 'subtitle_fr', 'supporters_count']

    if display_explanations:
        string_to_print += "<p>Retrait de lignes incomplètes</p><ul>"
    for col_name in essentials_columns_names:
        index = data.columns.get_loc(col_name)
        index_with_nan = data.index[data.iloc[:, index].isnull()]
        if display_explanations:
            string_to_print += "<li>Retrait de {} lignes n'ayant aucune valeur dans la colonne <strong>{}</strong></li>".format(
                len(index_with_nan), col_name)
        data.drop(labels=index_with_nan, inplace=True)
    if display_explanations:
        string_to_print += "</ul>"

    #Donnes textuelles
    summary_donnees_txt = """<p>Afin de traiter les données textuelles comme la description du projet, la description de l'auteur du projet ainsi que le titre et le sous-titre du projet, nous gardons seulement la longueur, le nombre de points d'exclamation et le nombre de points d'interrogations dans ces données</p>"""
    if display_explanations:
    	string_to_print += summary_donnees_txt   

    def clean_text(x):
    	return BeautifulSoup(x, "lxml").text
    def nb_exclamation(x):
    	return x.count('!')
    def nb_interogation(x):
    	return x.count('?')
    def prep_text(feature):
    	data['clean_'+feature] = data[feature].apply(clean_text)
    	data['len_'+feature] = data['clean_'+feature].apply(len)
    	data['nb_exclamation_'+feature]=data['clean_'+feature].apply(nb_exclamation)
    	data['nb_interogation_'+feature]=data['clean_'+feature].apply(nb_interogation)
    	data.drop(columns=[feature, 'clean_'+feature], inplace=True)

    prep_text('description_fr')
    prep_text('description_funding_fr')
    prep_text('description_yourself_fr')
    prep_text('name_fr')
    prep_text('subtitle_fr')

    # nb_days
    if display_explanations:
        nb_days = """<h5>nb_days</h5><p>La colonne "nb_days" contient un tiers de valeurs vides, il faut la compléter.</p>"""
        string_to_print += nb_days

    def days_between(d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)

    data['nb_days'] = [days_between(
        data.date_start[k][0:10], data.date_end[k][0:10]) for k in data.date_start.index]

    # news_per_days
    if display_explanations:
        string_to_print += "<h5>news_per_days</h5><p>Création de la colonne news_per_days</p>"
    col = (data["news_count"]/data["nb_days"]
           ).apply(lambda x: 0 if np.isnan(x) or np.isinf(x) else x)
    data["news_per_days"] = col
    zero_day_projects = data[data["nb_days"] == 0]
    # on enlève les projets ayant duré moins de 24h, il y en a 9 dont un seul financé
    data.drop(index=zero_day_projects.index, inplace=True)

    # nb_rewards
    if display_explanations:
        string_to_print += "<h5>nb_rewards</h5><p>Création de la colonne nb_rewards</p>"

    def get_nb_rewards(index_project):
        nb = 0
        for _ in data.rewards[index_project]:
            nb += len(data.rewards[index_project])
        return nb

    list_nb_reward = [get_nb_rewards(k) for k in data.rewards.index]
    data["nb_rewards"] = list_nb_reward

    # pre-post Covid
    if display_explanations:
        covid = """<h5>post_covid</h5><p>Nous allons étudier l'influence du COVID-19 sur les campagnes Ulule donc il est intéressant de rajouter une colonne 'post_covid' indiquant si le projet prend fin après le mois de mars 2020. Création de la colonne "post_covid"</p>"""
        string_to_print += covid
    date_covid = datetime.strptime('2020-03-01', '%Y-%m-%d')

    def post_covid(x):
        return datetime.strptime(x[:10], '%Y-%m-%d') > date_covid

    data['post_covid'] = data['date_end'].apply(post_covid)

    # date
    if display_explanations:
        date = """<h5>date_*</h5><>Il n'est plus utile de conserver les dates de début et de fin si on dispose des colonnes nb_days et post_covid. Retirons les.</p>"""
        string_to_print += date
    data.drop(columns=['date_start', 'date_end'], inplace=True)

    # type
    if display_explanations:
        type_project = """<h5>type</h5><p>Les projets fonctionnent différemment selon qu'ils concernent des préventes ou une financement. Il convient donc de séparer le set en deux sous-sets.</p>"""
        string_to_print += type_project
    data_presolds = data[data['type'] == 1]
    data = data[data['type'] == 2]

    # Strictement équivalent au nombre de participants
    if display_explanations:
        string_to_print += """<h5>nb_products_sold</h5><p>Retrait de la colonne <strong>nb_product_sold</strong> pour les projets n'étant pas sous la forme d'une prévente, car cette colonne est équivalente à la colonne <strong>supporters_count</strong>.</p>"""
    data.drop(columns="nb_products_sold", inplace=True)

    # Génération d'un CSV propre
    data_pre_covid, data_post_covid = generate_clean_data(data)

    print("-- Fin de la préparation")
    return data, data_pre_covid, data_post_covid, string_to_print


def generate_clean_data(data: DataFrame) -> Tuple[DataFrame, DataFrame]:
    """
    Extrait les données concernant les projets pré et post covid, génère des .CSV.

    La fonction sépare les données d'un dataframe en deux sous dataframe, selon
    la date du projet (si le projet est pré ou post covid). Les trois dataframe,
    en comptant l'original, sont exportés au format .CSV.

    Paramètres
    -------- 
    data : DataFrame
        Le dataframe contenant les données à séparer.

    Valeurs retournées
    -------- 
    data_pre_covid : DataFrame
        Les données des projets pre-covid.
    data_post_covid : DataFrame
        Les données des projets post-covid.
"""

    data_post_covid = data[data.post_covid == True].drop(
        columns=['post_covid'])
    data_pre_covid = data[data.post_covid == False].drop(
        columns=['post_covid'])

    # Génération d'un CSV propre
    if not os.path.isfile("./data/clean_data.csv"):
        data.to_csv('./data/clean_data.csv')
    if not os.path.isfile("./data/clean_data_post_covid.csv"):
        data_post_covid.to_csv('./data/clean_data_post_covid.csv')
    if not os.path.isfile("./data/clean_data_pre_covid.csv"):
        data_pre_covid.to_csv('./data/clean_data_pre_covid.csv')

    print("-- Fin de la génération des données nettoyées")

    return data_pre_covid, data_post_covid
