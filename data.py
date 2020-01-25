import pandas as pd


def read_data():
    data = pd.read_csv('dane.csv')
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
    print(popular_genre_with_plot_rnd)
