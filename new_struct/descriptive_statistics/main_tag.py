"""#TODO"""

import seaborn as sns
import pandas as pd
import markdown
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from new_struct.utils.utils import pie_feature


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    dict_percent_success = {}

    for index, main_tag in zip(data.main_tag.index, data.main_tag):
        goal_was_raised = 1 if data.goal_raised[index] else 0
        if main_tag["id"] not in dict_percent_success:
            dict_percent_success[main_tag["id"]] = [1, goal_was_raised]
        else:
            nb_project, nb_success = dict_percent_success[main_tag["id"]]
            nb_project += 1
            nb_success += goal_was_raised
            dict_percent_success[main_tag["id"]] = [nb_project, nb_success]

    for index, value in dict_percent_success.items():
        dict_percent_success[index] = value[1]/value[0]

    plt.figure(figsize=(10, 10))
    sns.boxplot(y=list(dict_percent_success.values()))
    plt.plot()
    print(markdown.markdown("""???"""))
