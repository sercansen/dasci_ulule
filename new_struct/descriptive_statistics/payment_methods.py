"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""
    pie_feature(data, "payment_methods",
                "Représentation des moyens de paiement autorisés par les projets")

    spearmanr(data['goal_raised'], data['payment_methods'])

    print(markdown.markdown("""La totalité autorise le trio "card, creditcard, saving" et 75% l'utilisent.
Il ne semble y avoir aucune corrélation entre le moyen de paiement et le succès de la campagne."""))
