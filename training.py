from collections import Counter

import pandas as pd
import numpy as np

from data import clean
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.linear_model import LogisticRegression


def split_a_set(popular_genre_with_plot_rnd):
    train = popular_genre_with_plot_rnd[:int(len(popular_genre_with_plot_rnd) * 0.8)]
    test = popular_genre_with_plot_rnd[int(len(popular_genre_with_plot_rnd) * 0.8):]

    train_x = train['Plot']
    train_y = train['Genre']

    test_x = test['Plot']
    test_y = test['Genre']

    train_y_encoded = pd.get_dummies(train_y)
    test_y_encoded = pd.get_dummies(test_y)

    train_x_cleaned = train_x.map(clean)
    test_x_cleaned = test_x.map(clean)
    return train_x_cleaned, test_x_cleaned, train_y, test_y


def tf_idf(popular_genre_with_plot_rnd, max_features_value):
    train_x_cleaned, test_x_cleaned, train_y, test_y = split_a_set(popular_genre_with_plot_rnd)
    tv = TfidfVectorizer(max_features=max_features_value)
    tv.fit(np.concatenate((train_x_cleaned.values, test_x_cleaned.values)))
    train_x_vectorized = tv.transform(train_x_cleaned)
    test_x_vectorized = tv.transform(test_x_cleaned)
    return tv, train_x_vectorized, test_x_vectorized, train_y, test_y


def do_logistic_regression(popular_genre_with_plot_rnd, plot):
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, None)
    lr = LogisticRegression(class_weight='balanced')
    lr.fit(train_x_vectorized, train_y)
    print(lr.score(test_x_vectorized, test_y))
    lr.predict(tv.transform([clean(plot)]))
    print(Counter(lr.predict(train_x_vectorized)).most_common())


def do_naive_bayes(popular_genre_with_plot_rnd, plot):
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, 5000)
    gnb = MultinomialNB()
    gnb.fit(train_x_vectorized.toarray(), train_y)
    print(gnb.score(test_x_vectorized.toarray(), test_y))
    print(Counter(gnb.predict(train_x_vectorized.toarray())).most_common())


def boosting():
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, 5000)

    # gbc = XGBClassifier(n_estimators=50)
    # gbc.fit(train_x_vectorized, train_y)
    # gbc.score(test_x_vectorized, test_y)


