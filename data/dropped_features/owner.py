"""#TODO"""

import matplotlib.pyplot as plt
from pandas import DataFrame


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>owner</h5>"

    # to_print += "<p>{}</p>".format([data.owner[k]['created_projects_online_count']
    #                                for k in data.owner.index])

    to_print += "<p>{}</p>".format(
        """A reprendre -> s'assurer que si un owner lance 44 projets, il n'apparaisse pas 44 fois dans le plot.""")
    return to_print
