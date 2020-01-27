from collections import Counter

from data import clean
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

from training import tf_idf


def do_logistic_regression(popular_genre_with_plot_rnd, plot):
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, None)
    lr = LogisticRegression(class_weight='balanced')
    lr.fit(train_x_vectorized, train_y)
    print('Skuteczność regresji logistycznej: {0:.2f}%'.format((lr.score(test_x_vectorized, test_y) * 100)))
    lr.predict(tv.transform([clean(plot)]))
    genre, _ = Counter(lr.predict(train_x_vectorized)).most_common(1)[0]
    return genre


def do_naive_bayes(popular_genre_with_plot_rnd, plot):
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, 5000)
    gnb = MultinomialNB()
    gnb.fit(train_x_vectorized.toarray(), train_y)
    print('Skuteczność naiwny Bayes: {0:.2f}%'.format((gnb.score(test_x_vectorized.toarray(), test_y)) * 100))
    gnb.predict(tv.transform([clean(plot)]).toarray())
    genre, _ = Counter(gnb.predict(train_x_vectorized.toarray())).most_common(1)[0]
    return genre


def do_boosting(popular_genre_with_plot_rnd, plot):
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, 1000)
    gbc = XGBClassifier(n_estimators=50)
    gbc.fit(train_x_vectorized, train_y)
    print('Skuteczność boosting: {0:.2f}%'.format((gbc.score(test_x_vectorized, test_y) * 100)))
    gbc.predict(tv.transform([clean(plot)]))
    genre, _ = Counter(gbc.predict(train_x_vectorized)).most_common(1)[0]
    return genre

