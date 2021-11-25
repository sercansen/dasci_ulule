""""""

import pdfkit
from data.data_preparation import prepare_data
from descriptive_statistics.post_covid import show_stats


def main():
    string_to_print = """<meta http-equiv="Content-type" content="text/html; charset=utf-8" />"""
    data, new_string = prepare_data(display_explanations=True)
    string_to_print += new_string
    pdfkit.from_string(string_to_print, './out.pdf',
                       css="./new_struct/styles/styles.css")
    print("-- Fin de la génération du pdf")


if __name__ == '__main__':
    main()
