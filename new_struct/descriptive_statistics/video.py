"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    pie_feature(data, "video", "Présence d'une vidéo dans le projet")

    plt.figure()
    sns.regplot(x="video", y="goal_raised", data=data)
    plt.show()

    spearmanr(data['goal_raised'], data['video'])
    print(markdown.markdown(
        """Il ne semble pas y avoir de corrélation entre le fait de posséder une vidéo et le succès de la campagne"""))
