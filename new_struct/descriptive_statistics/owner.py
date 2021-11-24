"""#TODO"""

import pandas as pd
import markdown


def show_stats(data: pd.DataFrame) -> None:
    """#TODO"""

    print([data.owner[k]['created_projects_online_count']
          for k in data.owner.index])
    print(markdown.markdown("""???"""))
