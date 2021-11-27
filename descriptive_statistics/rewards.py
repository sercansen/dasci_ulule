"""#TODO"""

import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from scipy.stats import spearmanr
from utils.utils import get_html_from_fig, plot_feature


def show_stats(data: DataFrame) -> None:
    """#TODO"""

    to_print = "<h5>rewards</h5>"
    fig = plot_feature(data, "nb_rewards", "", "", "")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    fig = plt.figure()
    sns.regplot(x="nb_rewards", y="goal_raised", data=data)
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        spearmanr(data['goal_raised'], data['nb_rewards']))
    to_print += "<p>{}</p>".format("""???""")

    to_print += "<p>{}</p>".format("""On appellera dans ce qui suit "meilleure récompense", la récompense maximisant le rapport de son prix sur le nombre d'achat. Ainsi une récompense vendue une seule fois à 500€ est meilleure qu'une récompense vendue 100 fois à 2€.""")

    def get_best_reward_index(project_index):
        rewards_outcomes_list = [reward["price"]*reward["stock_taken"]
                                 for reward in data.rewards[project_index]]
        index = rewards_outcomes_list.index(max(rewards_outcomes_list))
        return index

    best_reward_dict_price = {}
    best_reward_dict_nb = {}
    for index in data.rewards.index:
        index_reward = get_best_reward_index(index)
        best_reward_dict_price[index] = data.rewards[index][index_reward]["price"]
        best_reward_dict_nb[index] = data.rewards[index][index_reward]["stock_taken"]

    fig = plt.figure(figsize=(20, 10))
    list_prices = [best_reward_dict_price[key]
                   for key in sorted(best_reward_dict_price.keys())]
    list_nb = [best_reward_dict_nb[key]
               for key in sorted(best_reward_dict_nb.keys())]
    plt.loglog(list_prices, list_nb, '+')
    plt.xlabel("Prix de la meilleure récompense")
    plt.ylabel("Nombre de meilleure récompense vendues")
    plt.suptitle(
        "Représentation du nombre de meilleure récompense vendue par projet, en fonction de son prix")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format(
        """Les récompenses les plus rentables des projets semblent se situer entre 10 et 100€, pour une centaine de vente.""")

    percentage_best_reward = [best_reward_dict_nb[k]/data.supporters_count[k] if data.supporters_count[k] !=
                              0 and best_reward_dict_nb[k] <= data.supporters_count[k] else 0 for k in data.supporters_count.index]
    fig = plt.figure(figsize=(20, 10))
    plt.plot(data.id, percentage_best_reward, "+")
    plt.suptitle("Représentation de la place occupée par la meilleure récompense au sein de toutes les récompenses, par projet, en fonction de l'id du projet")
    plt.xlabel("Id du projet")
    plt.ylabel("Pourcentage occupé par la meilleure récompense")
    to_print += get_html_from_fig(fig)
    plt.close(fig)

    to_print += "<p>{}</p>".format("""???""")
    return to_print