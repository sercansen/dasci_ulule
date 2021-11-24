"""#TODO"""


import pandas as pd
import markdown
import data.dropped_features.comments_enabled as comments_enabled
import data.dropped_features.currency as currency
import data.dropped_features.date_end_extra_time as date_end_extra_time
import data.dropped_features.lang as lang
import data.dropped_features.lowest_contribution_amount as lowest_contribution_amount
import data.dropped_features.timezone as timezone


def get_dataframe_from_csv() -> pd.DataFrame:
    """#TODO """
    df = pd.read_csv("new_struct/data/ulule_data.csv", low_memory=False)
    print("-- Fin de la lecture des données.")
    return df


def understand_data(display_explanations: bool = False) -> pd.DataFrame:
    """#TODO"""

    data = get_dataframe_from_csv()

    drop_useless_columns_explanation = markdown.markdown("""## Vérification du set de données - Data understanding
    Dans la mesure où certains projets peuvent ou non avoir une vidéo de présentation, il est exclu de retirer toute ligne contenant un "NaN" (représentant un vide). On se contente donc de retirer les doublons et les colonnes constantes, dans un premier temps.""")
    if display_explanations:
        print(drop_useless_columns_explanation)
    # Retrait de doublons.
    data.drop_duplicates(inplace=True)
    # Retrait de colonnes constantes
    data = data.loc[:, (data != data.iloc[0]).any()]

    if display_explanations:
        set_analysis = markdown.markdown("""### Première analyse du set
        Le set contient près de 50000 lignes correspondant à des
        projets, réussis ou non, et 96 colonnes contenant différents éléments comme
        le montant levé ou la description du projet dans différentes langues.
        
        Les colonnes peuvent être groupées en quatre catégories :
        - les données construites par Ulule (comme des listes d'urls)
        - les données obsolètes ou constantes et qui seront retirées
        - les données liées au projet (avant le lancement)
        - les données liées à la campagne (après le lancement)
        
        #### Données construites par Ulule
        Ces données sont indépendantes du possesseur du projet (l'utilisateur que nous cherchons à conseiller) et <b>ne seront donc pas utilisées dans cette étude</b>.
        - ~absolute_url~
        - ~discussion_thread_id~
        - id
        - ~resource_uri~
        - ~slug~
        - ~urls~
        - ~user_role~

        L'id du projet sera conservé pour disposer d'une variable indépendante du projet et simple à représenter, en abscisse notamment.
        
        #### Données obsolètes ou inutiles
        Ces données proviennent d'anciennes versions de l'API ou sont constantes quelque soit le projet (dans ce data set) et sont donc à retirer.
        - ~address_required~
        - ~permissions~
        - ~phone_number_required~
        - ~required_personal_id_number~
        - ~image~
        - ~status~
        - ~is_in_extra_time~

        #### Données de la campagne
        Ces données concernent le projet après son lancement.

        - amount_raised
        - comments_count
        - ~committed~
        - date_end
        - date_end_extra_time
        - date_goal_raised
        - date_start
        - fans_count
        - ~finished~
        - ~is_cancelled~
        - ~is_in_extra_time~
        - ~lowest_contribution_amount~
        - nb_days
        - nb_products_sold
        - news_count
        - orders_count
        - percent
        - sponsorships_count
        - supporters_count
        - ~time_left~
        - ~time_left_short~

        Afin de ne pas biaiser notre modèle, nous ne nous intéresserons pas aux projets encore en cours. Les variables <b>time_left</b>, <b>time_left_short</b>, <b>is_in_extra_time</b> ainsi que <b>finished</b> (après le retrait des projets inachevés) ne sont donc pas pertinentes. De même, les projets annulés doivent être retirés, ainsi que la colonne <b>is_cancelled</b>.
        
        """)
        print(set_analysis)

        date_end_extra_time_txt = markdown.markdown("""##### date_end_extra_time
        La colonne date_end_extra_time sera retirée car aucun projet ayant échoué n'y a fait appel et c'est un phénomène très minoritaire.""")
        print(date_end_extra_time_txt)
        date_end_extra_time.show_stats(data)

        lowest_contribution_amount_txt = markdown.markdown("""##### lowest_contribution_amount
        Etant quasiment constante, la colonne <b>lowest_contribution_amount</b> peut également être retirée car non pertinente.""")
        print(lowest_contribution_amount_txt)
        lowest_contribution_amount.show_stats(data)

        committed = markdown.markdown("""##### committed
        La colonne committed concerne les promesses faites par les supporters. Il y a deux cas de figure :
        - Le projet est une campagne classique et les supporters promettent de l'argent (<b>amount_raised</b>) pour atteindre un objectif (<b>goal</b>). Dans ce cas, <b>committed</b> est strictement égal à <b>amount_raised</b>.
        - Le projet est une prévente, les supporters promettent d'acheter un nombre de produits (<b>nb_products_sold</b>) pour atteindre un objectif de vente (<b>goal</b>). Dans ce cas, <b>committed</b> est strictement égal à <b>nb_products_sold</b>.

        En conclusion, <b>committed</b> peut être retirée car inutile.""")
        print(committed)

        project_data = markdown.markdown("""#### Données du projet
        Ces données concernent le projet avant son lancement.

        - analytics_count
        - background
        - ~comments_enabled~
        - ~country~
        - ~currency~
        - ~currency_display~
        - delivery
        - ~description_ca~
        - ~description_de~
        - ~description_en~
        - ~description_es~
        - description_fr
        - ~description_it~
        - ~description_nl~
        - ~description_pt~
        - ~description_funding_ca~
        - ~description_funding_de~
        - ~description_funding_en~
        - ~description_funding_es~
        - description_funding_fr
        - ~description_funding_it~
        - ~description_funding_nl~
        - ~description_funding_pt~
        - goal
        - goal_raised
        - image
        - ~lang~
        - location
        - main_image
        - main_tag
        - ~name_ca~
        - ~name_de~
        - ~name_en~
        - ~name_es~
        - name_fr
        - ~name_it~
        - ~name_nl~
        - ~name_pt~
        - owner
        - payment_methods
        - rewards
        - sponsorships_count
        - ~subtitle_ca~
        - ~subtitle_de~
        - ~subtitle_en~
        - ~subtitle_es~
        - subtitle_fr
        - ~subtitle_it~
        - ~subtitle_nl~
        - ~subtitle_pt~
        - visible
        - video
        - type
        - ~timezone~
        
        Il ne nous a pas semblé pertinent de garder la colonne <b>delivery</b> car elle peut ne pas avoir de sens si le projet n'offre pas de récompense physique (comme un jeu vidéo ou un film).""")
        print(project_data)

        timezone_txt = markdown.markdown("""#####timezone
        L'immense majorité des projets a lieu dans la même zone, la colonne <b>timezone</b> est quasiment constante, elle peut être retirée.""")
        print(timezone_txt)
        timezone.show_stats(data)

        comments_enabled_txt = markdown.markdown("""##### comments_enabled
        Une écrasante majorité des projets autorise les commentaires pour tous les utilisateurs, la colonne <b>comments_enabled</b> n'est donc pas pertinente.""")
        print(comments_enabled_txt)
        comments_enabled.show_stats(data)

        currency_txt = markdown.markdown("""##### currency
        L'écrasante majorité des projets est en euro, il est donc possible de retirer la colonne <b>currency</b> ainsi que la colonne <b>currency_display</b>, sans oublier les projets concernés.""")
        print(currency_txt)
        currency.show_stats(data)

        lang_txt = markdown.markdown("""##### lang
        Les autres langues que le français étant très minoritaires, on peut retirer tous les projets concernés ainsi que les colonnes suivantes :
        - <b>description_[Langue!=fr]</b>
        - <b>description_funding_[Langue!=fr]</b>
        - <b>lang</b>
        - <b>name_[Langue!=fr]</b>
        - <b>subtitle_[Langue!=fr]</b>""")
        print(lang_txt)
        lang.show_stats(data)

    print("-- Fin de la compréhension")
    return data
