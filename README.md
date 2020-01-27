# predicting-the-movie-genre
Projekt o przewidywaniu gatunku filmu na podstawie opisu z Wikipedii. Dane treningowe pochodzą ze strony Kaggle (https://www.kaggle.com/jrobischon/wikipedia-movie-plots). Konieczne było oczyszczenie danych wykorzystując regular expressions.
Skorzystano z metody text miningu, jaką jest ważenie termów (TF-IDF). Czynnik TF oznacza częstość występowania słowa w danym tekście, czyli częstość termów, a czynnik IDF odwrotną częstość występowania i jest tym mniejszy, im dany wyraz częściej występuje w całym zbiorze dokumentów. W ten sposób wyróżniamy słowa, które mają dla nas znaczenie w analizie danego tekstu. 

Program wyznacza skuteczność poszczególnych klasyfikatorów i efekty na rzeczywistych przykładach. Możliwe klasyfikatory to regresja logistyczna, naiwny Bayes oraz boosting.

Program posiada prosty interfejs graficzny.
