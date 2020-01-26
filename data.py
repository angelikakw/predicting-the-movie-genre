import pandas as pd
import re

przypis_re = re.compile(r'\[[0-9]+\]')
number_re = re.compile(r'[0-9]+')
new_line_re = re.compile(r'\r\n')
new_line2_re = re.compile(r'\n\n')


def read_data(file_name):
    data = pd.read_csv(file_name)
    genre_counts = data[data['Genre'] != 'unknown']['Genre'].value_counts()

    popular_genre = []
    for name, count in genre_counts.iteritems():
        if count > 100:
            popular_genre.append(name)

    bools = []
    for elem in data['Genre']:
        if elem in popular_genre:
            bools.append(True)
        else:
            bools.append(False)

    popular_genre_with_plot = data[bools]
    popular_genre_with_plot_rnd = popular_genre_with_plot.sample(frac=1)
    return popular_genre_with_plot_rnd


def clean(plot):
    plot = re.sub(
        przypis_re,
        '',
        plot
    )

    plot = re.sub(
        new_line_re,
        ' ',
        plot
    )

    plot = re.sub(
        new_line2_re,
        ' ',
        plot
    )

    plot = re.sub(
        number_re,
        ' ',
        plot
    )

    return plot.replace('\'', '')