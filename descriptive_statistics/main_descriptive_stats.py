"""#TODO"""

from pandas import DataFrame
from descriptive_statistics.amount_raised import show_stats as amount_raised_show_stats
from descriptive_statistics.analytics_count import show_stats as analytics_count_show_stats
from descriptive_statistics.background import show_stats as background_show_stats
from descriptive_statistics.comments_count import show_stats as comments_count_show_stats
from descriptive_statistics.common_stats import show_stats as common_stats_show_stats
from descriptive_statistics.fans_count import show_stats as fans_count_show_stats
from descriptive_statistics.goal_raised import show_stats as goal_raised_show_stats
from descriptive_statistics.goal import show_stats as goal_show_stats
from descriptive_statistics.main_tag import show_stats as main_tag_show_stats
from descriptive_statistics.nb_days import show_stats as nb_days_show_stats
from descriptive_statistics.news_count import show_stats as news_count_show_stats
from descriptive_statistics.payment_methods import show_stats as payment_methods_show_stats
from descriptive_statistics.percent import show_stats as percent_show_stats
from descriptive_statistics.post_covid import show_stats as post_covid_show_stats
from descriptive_statistics.rewards import show_stats as rewards_show_stats
from descriptive_statistics.sponsorships_count import show_stats as sponsorships_count_show_stats
from descriptive_statistics.supporters_count import show_stats as supporters_count_show_stats
from descriptive_statistics.video import show_stats as video_show_stats
from descriptive_statistics.visible import show_stats as visible_show_stats


def show_stats(data: DataFrame, data_pre_covid: DataFrame, data_post_covid: DataFrame, data_general: DataFrame, are_stats_cat: bool) -> str:
    """#TODO : doc"""
    print("-- Début des statistiques descriptives")
    string_to_print = ""
    string_to_print += "<h2>Statistiques descriptives</h2>"
    string_to_print += amount_raised_show_stats(data)
    string_to_print += analytics_count_show_stats(data)
    string_to_print += background_show_stats(data)
    string_to_print += comments_count_show_stats(data)
    string_to_print += fans_count_show_stats(data)
    string_to_print += goal_raised_show_stats(data)
    string_to_print += goal_show_stats(data)
    string_to_print += nb_days_show_stats(data)
    string_to_print += news_count_show_stats(data)
    string_to_print += payment_methods_show_stats(data)
    string_to_print += percent_show_stats(data)
    string_to_print += post_covid_show_stats(data)
    string_to_print += rewards_show_stats(data)
    string_to_print += sponsorships_count_show_stats(data)
    string_to_print += supporters_count_show_stats(data)
    string_to_print += video_show_stats(data)
    string_to_print += visible_show_stats(data)
    string_to_print += common_stats_show_stats(
        data, data_pre_covid, data_post_covid, data_general, are_stats_cat)
    print("-- Fin des stats descriptives")
    return string_to_print
