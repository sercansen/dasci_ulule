"""#TODO"""

from pandas import DataFrame


def show_stats(data: DataFrame) -> str:
    """#TODO"""

    to_print = "<h5>owner</h5>"
    to_print += "<p>{}</p>".format([data.owner[k]['created_projects_online_count']
                                    for k in data.owner.index])
    to_print += "<p>{}</p>".format("""???""")
    return to_print
