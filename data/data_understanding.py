"""#TODO"""


from typing import Tuple
import pandas as pd
import data.dropped_features.comments_enabled as comments_enabled
import data.dropped_features.currency as currency
import data.dropped_features.date_end_extra_time as date_end_extra_time
import data.dropped_features.lang as lang
import data.dropped_features.lowest_contribution_amount as lowest_contribution_amount
import data.dropped_features.timezone as timezone


def _get_dataframe_from_csv() -> pd.DataFrame:
    """#TODO """
    df = pd.read_csv("data/ulule_data.csv", low_memory=False)
    print("-- Fin de la lecture des données")
    return df


def understand_data(display_explanations: bool = False) -> Tuple[pd.DataFrame, str]:
    """#TODO"""

    data = _get_dataframe_from_csv()

    string_to_print = """"""

    if display_explanations:
        drop_useless_columns_explanation = """<h2>Vérification du set de données - Data understanding</h2>
    <p>Dans la mesure où certains projets peuvent ou non avoir une vidéo de présentation, il est exclu de retirer toute ligne contenant un "NaN" (représentant un vide). On se contente donc de retirer les doublons et les colonnes constantes, dans un premier temps.</p>"""
        string_to_print += drop_useless_columns_explanation

    # Retrait de doublons.
    data.drop_duplicates(inplace=True)
    # Retrait de colonnes constantes
    data = data.loc[:, (data != data.iloc[0]).any()]

    if display_explanations:
        set_analysis = """<h3> Première analyse du set</h3>
        <p>Le set contient près de 50000 lignes correspondant à des
        projets, réussis ou non, et 96 colonnes contenant différents éléments comme
        le montant levé ou la description du projet dans différentes langues.</p>
        
        <p>Les colonnes peuvent être groupées en quatre catégories :</p>
        <ul>
            <li>les données construites par Ulule (comme des listes d'urls)</li>
            <li>les données obsolètes ou constantes et qui seront retirées</li>
            <li>les données liées au projet (avant le lancement)</li>
            <li>les données liées à la campagne (après le lancement)</li>
        </ul>
        
        <h4>Données construites par Ulule</h4>
        <p>Ces données sont indépendantes du possesseur du projet (l'utilisateur que nous cherchons à conseiller) et <strong>ne seront donc pas utilisées dans cette étude</strong>.</p>
        <ul>
            <li><del>absolute_url</del></li>
            <li><del>discussion_thread_id</del></li>
            <li>id</li>
            <li><del>resource_uri</del></li>
            <li><del>slug</del></li>
            <li><del>urls</del></li>
            <li><del>user_role</del></li>
        </ul>

        <p>L'id du projet sera conservé pour disposer d'une variable indépendante du projet et simple à représenter, en abscisse notamment.</p>
        
        <h4>Données obsolètes ou inutiles</h4>
        <p>Ces données proviennent d'anciennes versions de l'API ou sont constantes quelque soit le projet (dans ce data set) et sont donc à retirer.</p>
        <ul>
            <li><del>address_required</del></li>
            <li><del>permissions</del></li>
            <li><del>phone_number_required</del></li>
            <li><del>required_personal_id_number</del></li>
            <li><del>image</del></li>
            <li><del>status</del></li>
            <li><del>is_in_extra_time</del></li>
        </ul>

        <h4>Données de la campagne</h4>
        <p>Ces données concernent le projet après son lancement.</p>
        <ul>
            <li>amount_raised</li>
            <li>comments_count</li>
            <li><del>committed</del></li>
            <li>date_end</li>
            <li>date_end_extra_time</li>
            <li>date_goal_raised</li>
            <li>date_start</li>
            <li>fans_count</li>
            <li><del>finished</del></li>
            <li><del>is_cancelled</del></li>
            <li><del>is_in_extra_time</del></li>
            <li><del>lowest_contribution_amount</del></li>
            <li>nb_days</li>
            <li>nb_products_sold</li>
            <li>news_count</li>
            <li>orders_count</li>
            <li>percent</li>
            <li>sponsorships_count</li>
            <li>supporters_count</li>
            <li><del>time_left</del></li>
            <li><del>time_left_short</del></li>
        </ul>
        <p>Afin de ne pas biaiser notre modèle, nous ne nous intéresserons pas aux projets encore en cours. Les variables <strong>time_left</strong>, <strong>time_left_short</strong>, <strong>is_in_extra_time</strong> ainsi que <strong>finished</strong> (après le retrait des projets inachevés) ne sont donc pas pertinentes. De même, les projets annulés doivent être retirés, ainsi que la colonne <strong>is_cancelled</strong>.</p>
        """
        string_to_print += set_analysis

        string_to_print += date_end_extra_time.show_stats(data)

        string_to_print += lowest_contribution_amount.show_stats(data)

        committed = """<h5>committed</h5>
        <p>La colonne committed concerne les promesses faites par les supporters. Il y a deux cas de figure :</p>
        <ul>
            <li>Le projet est une campagne classique et les supporters promettent de l'argent (<strong>amount_raised</strong>) pour atteindre un objectif (<strong>goal</strong>). Dans ce cas, <strong>committed</strong> est strictement égal à <strong>amount_raised</strong>.</li>
            <li>Le projet est une prévente, les supporters promettent d'acheter un nombre de produits (<strong>nb_products_sold</strong>) pour atteindre un objectif de vente (<strong>goal</strong>). Dans ce cas, <strong>committed</strong> est strictement égal à <strong>nb_products_sold</strong>.</li>
        </ul>

        <p>En conclusion, <strong>committed</strong> peut être retirée car inutile.</p>"""
        string_to_print += committed

        project_data = """<h4>Données du projet</h4>
        <p>Ces données concernent le projet avant son lancement.</p>
        <ul>
            <li>analytics_count</li>
            <li>background</li>
            <li><del>comments_enabled</del></li>
            <li><del>country</del></li>
            <li><del>currency</del></li>
            <li><del>currency_display</del></li>
            <li>delivery</li>
            <li><del>description_ca</del></li>
            <li><del>description_de</del></li>
            <li><del>description_en</del></li>
            <li><del>description_es</del></li>
            <li>description_fr</li>
            <li><del>description_it</del></li>
            <li><del>description_nl</del></li>
            <li><del>description_pt</del></li>
            <li><del>description_funding_ca</del></li>
            <li><del>description_funding_de</del></li>
            <li><del>description_funding_en</del></li>
            <li><del>description_funding_es</del></li>
            <li>description_funding_fr</li>
            <li><del>description_funding_it</del></li>
            <li><del>description_funding_nl</del></li>
            <li><del>description_funding_pt</del></li>
            <li>goal</li>
            <li>goal_raised</li>
            <li>image</li>
            <li><del>lang</del></li>
            <li>location</li>
            <li>main_image</li>
            <li>main_tag</li>
            <li><del>name_ca</del></li>
            <li><del>name_de</del></li>
            <li><del>name_en</del></li>
            <li><del>name_es</del></li>
            <li>name_fr</li>
            <li><del>name_it</del></li>
            <li><del>name_nl</del></li>
            <li><del>name_pt</del></li>
            <li>owner</li>
            <li>payment_methods</li>
            <li>rewards</li>
            <li>sponsorships_count</li>
            <li><del>subtitle_ca</del></li>
            <li><del>subtitle_de</del></li>
            <li><del>subtitle_en</del></li>
            <li><del>subtitle_es</del></li>
            <li>subtitle_fr</li>
            <li><del>subtitle_it</del></li>
            <li><del>subtitle_nl</del></li>
            <li><del>subtitle_pt</del></li>
            <li>visible</li>
            <li>video</li>
            <li>type</li>
            <li><del>timezone</del></li>
        </ul>
        <p>Il ne nous a pas semblé pertinent de garder la colonne <strong>delivery</strong> car elle peut ne pas avoir de sens si le projet n'offre pas de récompense physique (comme un jeu vidéo ou un film).</p>"""
        string_to_print += project_data

        string_to_print += timezone.show_stats(data)

        string_to_print += comments_enabled.show_stats(data)

        string_to_print += currency.show_stats(data)

        string_to_print += lang.show_stats(data)

    print("-- Fin de la compréhension")
    return data, string_to_print
