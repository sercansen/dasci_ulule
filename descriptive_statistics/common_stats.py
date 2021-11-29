"""#TODO"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from utils.utils import get_html_from_fig


def show_stats(data: DataFrame, data_pre_covid: DataFrame, data_post_covid: DataFrame) -> str:
    """#TODO"""

    to_string = "<h4>Autres stats ? NOMMER CA AUTREMENT SVP</h4>"

    to_string += "<h5>Matrice de corrélation</h5>"
    corr_df = data.copy(deep=True)
    corr_df.drop(columns=['id', 'type', 'background', 'date_goal_raised', 'date_start', 'description_fr', 'description_funding_fr', 'description_yourself_fr',
                 'goal_raised', 'location', 'main_tag', 'name_fr', 'owner', 'payment_methods', 'rewards', 'subtitle_fr', 'video', 'visible'], inplace=True)
    fig = plt.figure(1)
    plt.matshow(corr_df.corr(), 1)

    def plot_corr(corr):
        plt.rc('figure', figsize=[15, 20])
        sns.heatmap(corr, annot=True, linewidth=0.5, square=True)

    plot_corr(corr_df.corr())

    to_string += get_html_from_fig(fig)
    plt.close(fig)

    to_string += "<p>{}</p>".format("""???""")

    to_string += "<h5>PCA</h5>"

    pre_covid_df = data_pre_covid.copy(deep=True)
    post_covid_df = data_post_covid.copy(deep=True)

    pre_covid_df.drop(columns=['id', 'date_end', 'date_goal_raised', 'date_start', 'description_fr', 'description_funding_fr', 'description_yourself_fr',
                      'goal_raised', 'location', 'main_tag', 'name_fr', 'owner', 'payment_methods', 'rewards', 'subtitle_fr', 'visible'], inplace=True)
    post_covid_df.drop(columns=['id', 'date_end', 'date_goal_raised', 'date_start', 'description_fr', 'description_funding_fr', 'description_yourself_fr',
                       'goal_raised', 'location', 'main_tag', 'name_fr', 'owner', 'payment_methods', 'rewards', 'subtitle_fr', 'visible'], inplace=True)

    x_pre_covid_scaled = StandardScaler().fit_transform(pre_covid_df.values)
    x_post_covid_scaled = StandardScaler().fit_transform(post_covid_df.values)

    pca_pre_cov = PCA().fit(x_pre_covid_scaled)
    pca_post_cov = PCA().fit(x_post_covid_scaled)

    components_pre_cov = pca_pre_cov.components_
    components_post_cov = pca_post_cov.components_

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = [20,10])
    circle1 = plt.Circle((0,0),1, fill = False)
    circle2 = plt.Circle((0,0),1, fill = False)

    for i, (x, y) in enumerate(zip(components_pre_cov[0,:], components_pre_cov[1,:])):
        ax1.plot([0, x], [0, y], color='b')
        ax1.text(x, y, pre_covid_df.columns[i], color='b')

    ax1.plot([-0.7, 0.7], [0, 0], color='grey', ls='--')
    ax1.plot([0, 0], [-0.7, 0.7], color='grey', ls='--')
    ax1.add_patch(circle1)
    ax1.set_title('Correlation circle for numerical features before March 2020')

    for i, (x, y) in enumerate(zip(components_post_cov[0,:], components_post_cov[1,:])):
        ax2.plot([0, x], [0, y], color='r')
        ax2.text(x, y, post_covid_df.columns[i], color='r')

    ax2.plot([-0.7, 0.7], [0, 0], color='grey', ls='--')
    ax2.plot([0, 0], [-0.7, 0.7], color='grey', ls='--')
    ax2.add_patch(circle2)
    ax2.set_title('Correlation circle for numerical features after March 2020')

    fig, ax = plt.subplots(figsize = [20,20])
    circle1 = plt.Circle((0,0),1, fill = False)
    circle2 = plt.Circle((0,0),1, fill = False)

    for i, (x, y) in enumerate(zip(components_pre_cov[0,:], components_pre_cov[1,:])):
        ax.plot([0, x], [0, y], color='b')
        ax.text(x, y, pre_covid_df.columns[i], color='b')

    ax.plot([-0.7, 0.7], [0, 0], color='grey', ls='--')
    ax.plot([0, 0], [-0.7, 0.7], color='grey', ls='--')
    ax.add_patch(circle1)
    ax.set_title('Correlation circle for numerical features before (blue) and after (red) March 2020')

    for i, (x, y) in enumerate(zip(components_post_cov[0,:], components_post_cov[1,:])):
        ax.plot([0, x], [0, y], color='r')
        ax.text(x, y, post_covid_df.columns[i], color='r')

    to_string += get_html_from_fig(fig)
    plt.close(fig)

    to_string += "<p>{}</p>".format("""???""")
    return to_string
