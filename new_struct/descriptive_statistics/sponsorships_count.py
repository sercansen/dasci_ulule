"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""
    pie_feature(data, "sponsorships_count",
                "Représentation du nombre de sponsors parmi les projets.")

    plt.figure()
    sns.regplot(x="sponsorships_count", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['sponsorships_count'])
    print(markdown.markdown("""L'obtention de sponsors semble être un phénomène très minoritaire.
Il ne semble pas y avoir de corrélation entre le succès de la campagne et la présence de sponsors."""))
