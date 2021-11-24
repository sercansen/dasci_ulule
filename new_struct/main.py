""""""

from data.data_preparation import prepare_data
from descriptive_statistics.post_covid import show_stats


def main():
    data = prepare_data(display_explanations=False)
    show_stats(data)


if __name__ == '__main__':
    main()
