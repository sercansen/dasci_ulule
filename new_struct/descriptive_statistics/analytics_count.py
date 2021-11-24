"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    plot_feature(data, "analytics_count", "Nombre d'analytics par projet",
                 "Identifiant du projet", "Nombre d'analytics")

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    sns.regplot(x="analytics_count", y="goal_raised", data=data, ax=ax1)

    f.suptitle("Succès du projet en fonction du nombre d'analytics")
    ax2.set_xlabel("Nombre d'analytics")
    ax2.set_ylabel("Succès du projet, 1=succès")
    ax2.plot(data.analytics_count, data.goal_raised, "+")
    plt.show()

    spearmanr(data['goal_raised'], data['analytics_count'])
    print(markdown.markdown(
        """On constate qu'il n'y a pas de corrélation entre le nombre d'analytics et la réussite d'un projet"""))
