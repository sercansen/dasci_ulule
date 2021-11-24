"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    pie_feature(data, "visible",
                "Indexation sur les moteurs de recherches du projet")

    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    sns.regplot(x="visible", y="goal_raised", data=data, ax=ax1)

    f.suptitle("Succès du projet en fonction de sa visibilité")
    ax2.set_xlabel("Visibilité")
    ax2.set_ylabel("Succès du projet, 1=succès")
    ax2.plot(data.visible, data.goal_raised, "+")
    plt.show()

    spearmanr(data['goal_raised'], data['visible'])
    print(markdown.markdown("""La plupart des projets sont indexés sur les moteurs de recherches.
On ne constate cepandant pas de corrélation entre la visibilité et le succès d'un projet"""))
