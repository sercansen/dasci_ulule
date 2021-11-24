"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature_log


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""
    plot_feature_log("comments_count", "Nombre de commentaires par projet",
                     "Identifiant du projet", "Nombres de commentaires")

    plt.figure()
    sns.regplot(x="comments_count", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['comments_count'])
    print(markdown.markdown("""Les projets reçoivent globalement assez peu de commentaires. La plupart des projets qui ont beaucoup de commentaires, ont bien fonctionné.
Il semble y avoir une petite corrélation entre le nombre de commentaires et le succès de la campagne."""))
