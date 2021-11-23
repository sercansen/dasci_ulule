""""""

from data.data_preparation import prepare_data


def main():
    data = prepare_data()
    print(data.columns)


if __name__ == '__main__':
    main()
