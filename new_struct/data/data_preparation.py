"""Ce fichier génère un dataframe bien cool"""


import markdown
import pandas as pd
import ast
from datetime import datetime
from data.data_understanding import understand_data

pd.set_option('display.max_columns', None)


def prepare_data(display_explanations=False) -> pd.DataFrame:
    data = understand_data(display_explanations=display_explanations)

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
        summary = markdown.markdown("""### Bilan : colonnes restantes
        Les colonnes suivantes sont conservées dans le dataset, mais peuvent nécessiter un travail supplémentaire, comme la colonne <b>video</b>. Nous n'allons en effet pas étudier la vidéo du projet en elle même mais plutôt le fait qu'elle existe ou non par exemple.

        Le set contient une trentaine de colonnes pour environs 40.000 projets.""")
        print(summary)
        print(data.columns)

    # Transformations de données
    # Binarisation
    summary_transformation = markdown.markdown(
        """Certaines colonnes doivent être binarisée pour représenter ou non la présence d'un objet (comme une vidéo).""")
    if display_explanations:
        print(summary_transformation)

    def binarize(x):
        return 1 if type(x) == str else 0

    data.background = data.background.apply(binarize)
    data.video = data.video.apply(binarize)

    # Owner
    if display_explanations:
        owner = markdown.markdown(
            "La colonne owner est inutilisable en tant que telle car seules les stats <b>anonymisées et concernant l'activité publique de lancement de projet</b> de l'owner nous intéressent.")
        print(owner)

    def recup_in_str_owner(x):
        return ast.literal_eval(x['owner'])['stats']

    data['owner'] = data.apply(recup_in_str_owner, axis=1)

    # Rewards
    if display_explanations:
        rewards = markdown.markdown("""Pour chaque projet, l'attribut reward propose un certain nombre de rewards dans une liste. Pour chaque reward, plusieurs informations sont disponibles, comme une date de livraison, un nombre de stock etc. Il est possible pour une reward d'avoir plusieurs variantes, par exemple une couleur pour un T-shirt, localisé dans l'attribut 'variants'.

        Les stocks seront toujours nuls (les projets sont finis) mais il est possible de savoir combien de chacune des rewards ont été prises, et à quel prix. Il est donc possible de voir, pour un projet, ce qui a été le plus rentable i.e. plein de petites rewards ou peu de grosses; et de croiser avec tous les autres projets.

        La colonne doit donc être retravaillée pour extraire une liste de dictionnaires par projet.""")
        print(rewards)

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
        main_tag = markdown.markdown("""##### main_tag
Dans la mesure où les projets ne se comportent pas de la même façon selon leur type, il peut être intéressant d'étudier les tags utilisés pour les décrire. Seuls nous intéressent l'id et le nom en français du tag, il faut donc les extraire.""")
        print(main_tag)

    def recup_in_str_main_tag(x):
        if type(x["main_tag"]) == str:
            return {key: val for key, val in ast.literal_eval(x["main_tag"]).items() if key == 'name_fr' or key == 'id'}

    data["main_tag"] = data.apply(recup_in_str_main_tag, axis=1)

    # Retrait de lignes incomplètes
    essentials_columns_names = ['date_start', 'date_end', 'amount_raised', 'comments_count', 'date_start', 'date_end', 'description_fr',
                                'description_funding_fr', 'description_yourself_fr', 'fans_count',
                                'goal', 'goal_raised', 'id', 'main_tag', 'name_fr', 'news_count', 'owner', 'percent',
                                'rewards', 'sponsorships_count', 'subtitle_fr', 'supporters_count']

    for col_name in essentials_columns_names:
        index = data.columns.get_loc(col_name)
        index_with_nan = data.index[data.iloc[:, index].isnull()]
        if display_explanations:
            print("Retrait de {} lignes n'ayant aucun valeur dans la colonne {}".format(
                len(index_with_nan), col_name))
        data.drop(labels=index_with_nan, inplace=True)

    # nb_days
    if display_explanations:
        nb_days = markdown.markdown(
            """La colonne "nb_days" contient un tiers de valeurs vides, il faut la compléter.""")
        print(nb_days)

    def days_between(d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)

    data['nb_days'] = [days_between(
        data.date_start[k][0:10], data.date_end[k][0:10]) for k in data.date_start.index]

    # pre-post Covid
    if display_explanations:
        covid = markdown.markdown(
            """Nous allons étudier l'influence du COVID-19 sur les campagnes Ulule donc il est intéressant de rajouter une colonne 'post_covid' indiquant si le projet prend fin après le mois de mars 2020.""")
        print(covid)
    date_covid = datetime.strptime('2020-03-01', '%Y-%m-%d')

    def post_covid(x):
        return datetime.strptime(x[:10], '%Y-%m-%d') > date_covid

    data['post_covid'] = data['date_end'].apply(post_covid)

    # type
    if display_explanations:
        type_project = markdown.markdown(
            """Les projets fonctionnent différemment selon qu'ils concernent des préventes ou une financement. Il convient donc de séparer le set en deux sous-sets.""")
        print(type_project)
    data_presolds = data[data['type'] == 1]
    data = data[data['type'] == 2]

    # Strictement équivalent au nombre de participants
    data.drop(columns="nb_products_sold", inplace=True)

    return data
