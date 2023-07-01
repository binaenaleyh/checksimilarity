from math import exp, sqrt
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


def squared_sum(x):
    return round(sqrt(sum([a*a for a in x])), 3)


# Similarity Methods
def cosinus_similarity(x, y):
    numerator = sum(a*b for a, b in zip(x, y))
    denominator = squared_sum(x)*squared_sum(y)

    return round(numerator/float(denominator), 2)


def euclidean_distance(x, y):
    distance = sqrt(sum(pow(a-b, 2) for a, b in zip(x, y)))
    similarity = 1/exp(distance)

    return similarity


def jaccard_similarity(x, y):
    intersection = len(set.intersection(*[set(x), set(y)]))
    union = len(set.union(*[set(x), set(y)]))

    return intersection/float(union)


# Vectorizing Methods
def tfidf_vectorize(x, y):
    vectorizer = TfidfVectorizer()
    encoded = vectorizer.fit_transform([x, y])

    return encoded.toarray()


def count_vectorize(x, y):
    vectorizer = CountVectorizer()
    encoded = vectorizer.fit_transform([x, y])

    return encoded.toarray()