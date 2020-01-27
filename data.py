import pandas as pd
import re

FOORNOTE_RE = re.compile(r'\[[0-9]+\]')
NUMBER_RE = re.compile(r'[0-9]+')
NEW_LINE_RE = re.compile(r'\r\n')
NEW_LINE_2_RE = re.compile(r'\n\n')


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
        FOORNOTE_RE,
        '',
        plot
    )

    plot = re.sub(
        NEW_LINE_RE,
        ' ',
        plot
    )

    plot = re.sub(
        NEW_LINE_2_RE,
        ' ',
        plot
    )

    plot = re.sub(
        NUMBER_RE,
        ' ',
        plot
    )

    return plot.replace('\'', '')