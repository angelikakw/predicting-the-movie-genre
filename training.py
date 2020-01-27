import numpy as np

from data import clean
from sklearn.feature_extraction.text import TfidfVectorizer


def split_a_set(popular_genre_with_plot_rnd):
    train = popular_genre_with_plot_rnd[:int(len(popular_genre_with_plot_rnd) * 0.8)]
    test = popular_genre_with_plot_rnd[int(len(popular_genre_with_plot_rnd) * 0.8):]

    train_x = train['Plot']
    train_y = train['Genre']

    test_x = test['Plot']
    test_y = test['Genre']

    train_x_cleaned = train_x.map(clean)
    test_x_cleaned = test_x.map(clean)
    return train_x_cleaned, test_x_cleaned, train_y, test_y


def tf_idf(popular_genre_with_plot_rnd, max_features_value):

    """ Function calculate term frequency–inverse document frequency (TF-IDF) """

    train_x_cleaned, test_x_cleaned, train_y, test_y = split_a_set(popular_genre_with_plot_rnd)
    tv = TfidfVectorizer(max_features=max_features_value)
    tv.fit(np.concatenate((train_x_cleaned.values, test_x_cleaned.values)))
    train_x_vectorized = tv.transform(train_x_cleaned)
    test_x_vectorized = tv.transform(test_x_cleaned)
    return tv, train_x_vectorized, test_x_vectorized, train_y, test_y







