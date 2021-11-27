"""#TODO"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

from utils.utils import get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_string = "<h4>Autres stats ? NOMMER CA AUTREMENT SVP</h4>"
    corr_df = data.copy(deep=True)
    corr_df.drop(columns=['id', 'type', 'background', 'date_goal_raised', 'date_start', 'description_fr', 'description_funding_fr', 'description_yourself_fr',
                 'goal_raised', 'location', 'main_tag', 'name_fr', 'owner', 'payment_methods', 'rewards', 'subtitle_fr', 'video', 'visible'], inplace=True)
    fig = plt.figure(1)
    plt.matshow(corr_df.corr(), 1)

    def plot_corr(corr):
        plt.rc('figure', figsize=[15, 15])
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        sns.heatmap(corr, mask=mask, cmap=cmap,
                    annot=True, linewidth=0.5, square=True)

    plot_corr(corr_df.corr())
    to_string += get_html_from_fig(fig)
    plt.close(fig)

    to_string += "<p>{}</p>".format("""???""")
    return to_string
