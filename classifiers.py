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
    print(lr.score(test_x_vectorized, test_y))
    lr.predict(tv.transform([clean(plot)]))
    print(Counter(lr.predict(train_x_vectorized)).most_common())


def do_naive_bayes(popular_genre_with_plot_rnd, plot):
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, 5000)
    gnb = MultinomialNB()
    gnb.fit(train_x_vectorized.toarray(), train_y)
    print(gnb.score(test_x_vectorized.toarray(), test_y))
    gnb.predict(tv.transform([clean(plot)]).toarray())
    print(Counter(gnb.predict(train_x_vectorized.toarray())).most_common())


def do_boosting(popular_genre_with_plot_rnd, plot):
    tv, train_x_vectorized, test_x_vectorized, train_y, test_y = tf_idf(popular_genre_with_plot_rnd, 1000)
    gbc = XGBClassifier(n_estimators=50)
    gbc.fit(train_x_vectorized, train_y)
    print(gbc.score(test_x_vectorized, test_y))
    gbc.predict(tv.transform([clean(plot)]))
    print(Counter(gbc.predict(train_x_vectorized)).most_common())