"""Fonction utiles lel"""

import matplotlib.pyplot as plt
import seaborn as sns


def pie_feature(data, feature_name, title):
    plt.figure()
    plt.suptitle(title)
    # on compte le nombre de personnes qui ont chaque feature
    valeurs = data[feature_name].value_counts()
    plt.pie(valeurs, labels=valeurs.index, autopct='%1.2f%%')
    plt.show()


def plot_feature(data, feature_name, title, xlabel, ylabel):
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    plt.suptitle(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.plot(data.id, data[feature_name], "+")

    sns.boxplot(y=data[feature_name], ax=ax2)
    ax2.set_ylabel("")
    plt.show()
