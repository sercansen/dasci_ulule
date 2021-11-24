"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature_log


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    plot_feature_log(data, "goal", "Objectif de validation du projet",
                     "Identifiant du projet", "Objectif euros")

    plt.figure()
    sns.regplot(x="goal", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['goal'])
    print(markdown.markdown("""La majorité des projets semble se concentrer autour de la même fourchette de valeur, malgré quelques valeurs extrêmes.
Il ne semble pas y avoir de corrélation entre le montant de succès de la campagne et son succès."""))
