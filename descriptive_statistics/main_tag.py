"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from utils.utils import get_html_from_fig


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>success_percent_per_main_tag</h5>"
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

    fig = plt.figure(figsize=(10, 10))
    sns.boxplot(y=list(dict_percent_success.values()))
    to_print += get_html_from_fig(fig)
    plt.close(fig)
    to_print += "<p>{}</p>".format("???")
    return to_print
