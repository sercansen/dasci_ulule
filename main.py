"""
Point d'entrée du programme, charge le ou les CSV, lance les stats.

Fonctions
----------
main
    S'occupe du chargement des CSV, des stats et de la génération du pdf.
"""

from descriptive_statistics.main_descriptive_stats import show_stats
from data.data_preparation import generate_clean_data_cat_all, prepare_data
from data.data_load import load_clean_data, load_post_covid_data, load_pre_covid_data, load_categorical_data
import os
import pdfkit
import warnings

from ml_models.main_machine_learning import machine_learning
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def main(display_explanations=False) -> None:
    """
    Fonction chargée de déclencher l'appel aux différentes sous-programmes.>

    La fonction est chargée entre autres de charger les fichiers CSV,
    d'afficher les stats descriptives, et de générer le pdf de sortie.

    Paramètres
    -------- 
    display_explanations : bool, optionnel
        Indique au programme s'il doit afficher les explications de ce qui est
        fait dans le pdf de sortie ou non (utile pour accélérer le programme
        lors d'un débuggage).
    """

    print("Souhaitez-vous faire l'analyse de toutes les données (entrez 'tout') ou seulement d'une catégorie (entrez 'cat') ?")
    x = input()
    print("Vous avez choisi ", x)
    y = "tout"

    if x == 'cat':
        tags_possibles = ["Solidaire & Citoyen",
                          "Santé & Bien-être",
                          "Artisanat & Cuisine",
                          "Art & Photo",
                          "Edition & Journal.",
                          "BD",
                          "Autres projets",
                          "Musique",
                          "Mode & Design",
                          "Film et vidéo",
                          "Jeux",
                          "Spectacle vivant",
                          "Sports",
                          "Technologie",
                          "Patrimoine",
                          "Enfance & Educ."]

        print("Entrer le main_tag parmi les suivants : (pour l'analyse de toutes les données, tapez 'tout')")
        for tag in tags_possibles:
            print(tag, end="  ")
        print("\n")
        y = input()
        if y in tags_possibles:
            print("Vous avez choisi ", y)

            file_name = "data/data_cat_covid/data_" + y + "/clean_data_" + y + ".csv"
            file_name_pre_covid = "data/data_cat_covid/data_" + \
                y + "/pre_covid_data_" + y + ".csv"
            file_name_post_covid = "data/data_cat_covid/data_" + \
                y + "/post_covid_data_" + y + ".csv"

        elif y == 'tout':
            print("Vous avez choisi ", y)

        else:
            print("Erreur")
            return

    string_to_print = """<meta http-equiv="Content-type" content="text/html; charset=utf-8" />"""

    # Introduction
    if display_explanations:
        string_to_print += """<img src="https://www.imt-atlantique.fr/sites/default/files/Images/Ecole/charte-graphique/IMT_Atlantique_logo_RVB_Baseline_400x272.jpg">"""
        string_to_print += """<h1>Journey to Data Scientist : le cas Ulule</h1>"""
        string_to_print += """<h2>Introduction - Business understanding</h2><p>Dans la présente étude nous nous considérons comme une équipe de data scientists travaillant pour Ulule. L'objectif sera d'élaborer un modèle de machine learning permettant de prédire ou non le succès d'une campagne de crowdfunding à partir de données de la campagne; et de conseiller l'utilisateur derrière la campagne sur ce qu'il peut améliorer.</p>
        <p>Dans la mesure où Ulule se rémunère en touchant une commission sur les projets ayant fonctionné, le site a tout intérêt à ce qu'un maximum de projets réussissent.</p>"""
        string_to_print += """<h5>Note :</h5><p>Cette étude est basée principalement sur un set de données obtenu via l'API publique d'Ulule, avec l'autorisation du site par e-mail.
Une vérification du set sera effectuée afin de ne pas traiter de données personnelles.</p>"""

    # Chargement des données générales
    print("- Début du chargement des données")
    if os.path.isfile("./data/clean_data.csv"):
        string_to_print += "<h2>Chargement des données du CSV pré-nettoyé</h2>"
        data = load_clean_data()
        data_pre_covid = load_pre_covid_data()
        data_post_covid = load_post_covid_data()
        print("-- Début du chargement des données catégorielles")
        dict_df_cat = generate_clean_data_cat_all(
            data, data_pre_covid, data_post_covid)
        print("-- Fin du chargement des données catégorielles")
    else:
        print("-- Début de la préparation des données")
        data, data_pre_covid, data_post_covid, dict_df_cat, new_string = prepare_data(
            display_explanations=display_explanations)
        string_to_print += new_string
        print("-- Fin de la préparation des données")
    print("- Fin du chargement des données")

    # Affichage des statistiques descriptives
    if display_explanations:
        if x != "tout" and y != "tout":
            data_cat = dict_df_cat["data_" + y]
            data_cat_pre_covid = dict_df_cat["data_pre_covid_" + y]
            data_cat_post_covid = dict_df_cat["data_post_covid_" + y]
            string_to_print += show_stats(data_cat, data_cat_pre_covid,
                                          data_cat_post_covid, data, True)
        else:
            string_to_print += show_stats(data, data_pre_covid,
                                          data_post_covid, data, False)

    # Machine Learning
    print("- Début du machine learning")
    string_to_print += machine_learning(y, data,
                                        data_pre_covid, data_post_covid, dict_df_cat)
    print("- Fin du machine learning")

    # Génération du pdf de sortie
    print("- Début de la génération du pdf")
    pdfkit_safe_name = {"tout": "tout",
                        "Solidaire & Citoyen": "solidaire_citoyen",
                        "Santé & Bien-être": "sante_bien_etre",
                        "Artisanat & Cuisine": "artisanat_cuisine",
                        "Art & Photo": "art_photo",
                        "Edition & Journal.": "edition_journal",
                        "BD": "bd",
                        "Autres projets": "autres",
                        "Musique": "musique",
                        "Mode & Design": "mode_design",
                        "Film et vidéo": "film_video",
                        "Jeux": "jeux",
                        "Spectacle vivant": "spectacle",
                        "Sports": "sports",
                        "Technologie": "technologie",
                        "Patrimoine": "patrimoine",
                        "Enfance & Educ.": "enfance_educ"}
    output_file_name = "out/" + pdfkit_safe_name[y] + ".pdf"
    pdfkit.from_string(string_to_print, output_path=output_file_name,
                       css="./styles/styles.css")
    print("- Fin de la génération du pdf")


if __name__ == '__main__':
    main(display_explanations=True)
