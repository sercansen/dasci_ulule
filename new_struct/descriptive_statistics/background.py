"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    pie_feature(data, "background", "Présence d'un background dans le projet")

    plt.figure()
    sns.regplot(x="background", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['background'])
    print(markdown.markdown(
        """Il n'y a pas de corrélation entre la présence d'un background et le succès de la campagne."""))
