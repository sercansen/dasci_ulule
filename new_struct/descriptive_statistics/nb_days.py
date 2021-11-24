"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    plot_feature(data, "nb_days", "Durée de la campagne de financement",
                 "Identifiant du projet", "Nombre de jours")

    plt.figure()
    sns.regplot(x="nb_days", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['nb_days'])

    print(markdown.markdown("""Les campagnes semblent durer plus ou moins un mois en grande majorité.
Il ne semble n'y avoir aucune corrélation entre la durée de la campagne et son succès."""))
