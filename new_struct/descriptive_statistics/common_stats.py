"""#TODO"""

import seaborn as sns
import pandas as pd
import numpy as np
import markdown
import matplotlib.pyplot as plt


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    corr_df = data.copy(deep=True)
    corr_df.drop(columns=['id', 'type', 'background', 'date_goal_raised', 'date_start', 'description_fr', 'description_funding_fr', 'description_yourself_fr',
                 'goal_raised', 'location', 'main_tag', 'name_fr', 'owner', 'payment_methods', 'rewards', 'subtitle_fr', 'video', 'visible'], inplace=True)
    plt.matshow(corr_df.corr())

    def plot_corr(corr):
        plt.rc('figure', figsize=[15, 15])
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        sns.heatmap(corr, mask=mask, cmap=cmap,
                    annot=True, linewidth=0.5, square=True)
        plt.show()

    plot_corr(corr_df.corr())

    print(markdown.markdown("""???"""))
