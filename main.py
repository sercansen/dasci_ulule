"""
Point d'entrée du programme, charge le ou les CSV, lance les stats.

Fonctions
----------
main
    S'occupe du chargement des CSV, des stats et de la génération du pdf
"""

from descriptive_statistics.main_descriptive_stats import show_stats
from data.data_preparation import prepare_data
from data.data_load import load_clean_data, load_post_covid_data, load_pre_covid_data
import os
import pdfkit


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

    string_to_print = """<meta http-equiv="Content-type" content="text/html; charset=utf-8" />"""

    # Introduction
    if display_explanations:
        string_to_print += """<img src="https://www.imt-atlantique.fr/sites/default/files/Images/Ecole/charte-graphique/IMT_Atlantique_logo_RVB_Baseline_400x272.jpg">"""
        string_to_print += """<h1>Journey to Data Scientist : le cas Ulule</h1>"""
        string_to_print += """<h2>Introduction - Business understanding</h2><p>Dans la présente étude nous nous considérons comme une équipe de data scientists travaillant pour Ulule. L'objectif sera d'élaborer un modèle de machine learning permettant de prédire ou non le succès d'une campagne de crowdfunding à partir de données de la campagne; et de conseiller l'utilisateur derrière la campagne sur ce qu'il peut améliorer.</p>
        <p>Dans la mesure où Ulule se rémunère en touchant une commission sur les projets ayant fonctionné, le site a tout intérêt à ce qu'un maximum de projets réussissent.</p>"""
        string_to_print += """<h5>Note :</h5><p>Cette étude est basée principalement sur un set de données obtenu via l'API publique d'Ulule, avec l'autorisation du site par e-mail.
Une vérification du set sera effectuée afin de ne pas traiter de données personnelles.</p>"""

    # Chargement des données
    if os.path.isfile("./data/clean_data.csv"):
        print("-- Début du chargement des données nettoyées")
        string_to_print += "<h2>Chargement des données du CSV pré-nettoyé</h2>"
        data = load_clean_data()
        data_pre_covid = load_pre_covid_data()
        data_post_covid = load_post_covid_data()
        print("-- Fin du chargement des données")
    else:
        print("-- Début de la préparation des données")
        data, data_pre_covid, data_post_covid, new_string = prepare_data(
            display_explanations=display_explanations)
        string_to_print += new_string
        print("-- Fin de la préparation des données")

    # Affichage des statistiques descriptives
    if display_explanations:
        string_to_print += show_stats(data, data_pre_covid,
                                      data_post_covid)

    # Génération du pdf de sortie
    pdfkit.from_string(string_to_print, './out.pdf',
                       css="./styles/styles.css")
    print("-- Fin de la génération du pdf")


if __name__ == '__main__':
    main(display_explanations=True)
