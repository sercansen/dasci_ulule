"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""
    plot_feature(data, "fans_count",
                 "Représentation du nombre de fans", "Id du projet", "Nombre de fans")

    plt.figure()
    sns.regplot(x="fans_count", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['fans_count'])

    print(markdown.markdown("""La présence de fans semble être un phénomène très minoritaire, il serait intéressant de vérifier si les projets suivis ont été plus réussis que les autres.
Il est possible de conclure quand à l'existence d'une corrélation entre le succès de la campagne et le nombre de fans."""))
