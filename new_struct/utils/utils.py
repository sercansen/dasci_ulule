"""Fonction utiles lel"""


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import base64
from matplotlib.figure import Figure
from io import BytesIO


def pie_feature(data: pd.DataFrame, feature_name: str, title: str) -> Figure:
    fig = plt.figure()
    plt.suptitle(title)
    # on compte le nombre de personnes qui ont chaque feature
    valeurs = data[feature_name].value_counts()
    plt.pie(valeurs, labels=valeurs.index, autopct='%1.2f%%')
    return fig


def plot_feature(data, feature_name, title, xlabel, ylabel):
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    plt.suptitle(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.plot(data.id, data[feature_name], "+")

    sns.boxplot(y=data[feature_name], ax=ax2)
    ax2.set_ylabel("")
    return f


def plot_feature_log(data, feature_name, title, xlabel, ylabel):
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


def get_html_from_fig(fig):
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
    return html
