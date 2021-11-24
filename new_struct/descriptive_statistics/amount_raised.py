"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature_log


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    plot_feature_log("amount_raised", "Montant levé par projet",
                     "Identifiant du projet", "Montant levé en euros")

    plt.figure()
    sns.regplot(x="amount_raised", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['amount_raised'])

    print(markdown.markdown("""Les projets semblent assez homogènes dans les montants levés même si moins nombreux pour les plus hauts montants.
Il semble y avoir une bonne corrélation entre le montant obtenu et le succès de la campagne (peu surprenant)."""))
