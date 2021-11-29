"""
Module contenant des fonction utiles à l'ensemble du programme.

Fonctions
----------
pie_feature
    Affiche les données d'une colonne d'un DataFrame dans un pie chart.
plot_feature
    Affiche les données d'une colonne d'un DataFrame dans un plot.
plot_feature_log
    Affiche les données d'une colonne d'un DataFrame dans un plot, en échelle log.
get_html_from_fig
    Génère le code HTML à afficher dans le pdf de sortie.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import base64
from pandas import DataFrame
from matplotlib.figure import Figure
from io import BytesIO

pourcentage_limite = 1


def _my_autopct(pct):
    """Améliore l'affichage des pourcentages des piecharts."""
    return ('%.2f' % pct) if pct > pourcentage_limite else ''


def pie_feature(data: DataFrame, feature_name: str, title: str) -> Figure:
    """
    Génère un pie chart à partir d'une colonne d'un data frame, et d'un titre.

    Paramètres
    -------- 
    data : DataFrame
        Le dataFrame contenant les données utilisées pour le pie chart.
    feature_name : str
        Le nom de la colonne à utiliser dans le dataFrame.
    title : str
        Le titre du graphe.

    Valeurs retournées
    -------- 
    fig : Fig
        La figure générée par Matplotlib contenant le graphe.
    """

    fig = plt.figure()
    plt.suptitle(title)
    # on compte le nombre de personnes qui ont chaque feature
    valeurs = data[feature_name].value_counts()
    label = [n if v > valeurs.sum()*pourcentage_limite/100 else '' for n,
             v in zip(valeurs.index, valeurs)]

    plt.pie(valeurs, labels=label, autopct=_my_autopct)
    return fig


def plot_feature(data: DataFrame, feature_name: str, title: str, xlabel: str, ylabel: str) -> Figure:
    """
    Génère un graphe à partir d'une colonne d'un data frame, d'un titre et de noms d'axes.

    Paramètres
    -------- 
    data : DataFrame
        Le dataFrame contenant les données utilisées pour le pie chart.
    feature_name : str
        Le nom de la colonne à utiliser dans le dataFrame.
    title : str
        Le titre du graphe.
    xlabel : str
        Le titre de l'axe des x.
    ylabel : str
        Le titre de l'axe des y.

    Valeurs retournées
    -------- 
    fig : Fig
        La figure générée par Matplotlib contenant le graphe.
    """

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    plt.suptitle(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.plot(data.id, data[feature_name], "+")

    sns.boxplot(y=data[feature_name], ax=ax2)
    ax2.set_ylabel("")
    return f


def plot_feature_log(data: DataFrame, feature_name: str, title: str, xlabel: str, ylabel: str) -> Figure:
    """
    Génère un graphe à partir d'une colonne d'un data frame, d'un titre et de noms d'axes.

    Le graphe est en échelle log.

    Paramètres
    -------- 
    data : DataFrame
        Le dataFrame contenant les données utilisées pour le pie chart.
    feature_name : str
        Le nom de la colonne à utiliser dans le dataFrame.
    title : str
        Le titre du graphe.
    xlabel : str
        Le titre de l'axe des x.
    ylabel : str
        Le titre de l'axe des y.

    Valeurs retournées
    -------- 
    fig : Fig
        La figure générée par Matplotlib contenant le graphe.
    """

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    plt.suptitle(title)
    ax1.set_yscale("log")
    ax2.set_yscale("log")
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.plot(data.id, data[feature_name], "+")

    sns.boxplot(y=data[feature_name], ax=ax2)
    ax2.set_ylabel("")
    return f


def get_html_from_fig(fig: Figure) -> str:
    """
    Génère un code HTML contenant le graph présent sur une figure matplotlib.

    Paramètres
    -------- 
    fig : Figure
        La figure contenant le graphe.

    Valeurs retournées
    -------- 
    html : str
        Le code HTML contenant le graphe.
    """

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
    return html
