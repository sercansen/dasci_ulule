"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import plot_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    plot_feature(data, "supporters_count", "Nombre de supporters par projet",
                 "Identifiant du projet", "Nombre de supporters")

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    sns.regplot(x="supporters_count", y="goal_raised", data=data, ax=ax1)

    f.suptitle("Succès du projet en fonction du nombre de supporters")
    ax2.set_xlabel("Nombre de supporters")
    ax2.set_ylabel("Succès du projet, 1=succès")
    ax2.plot(data.supporters_count, data.goal_raised, "+")
    plt.show()

    spearmanr(data['goal_raised'], data['supporters_count'])
    print(markdown.markdown(
        """On constate une bonne corrélation entre le succès du projet et le nombre de supporters."""))
