from enum import Enum
from pydantic import BaseModel, Field

from functions import *


class VectorizingMethod(str, Enum):
    TFIDF = "TF-IDF"
    COUNT = "Count Vectorizer"


class SimilarityMethod(str, Enum):
    COSINE = "Cosine Similarity"
    EUCLID = "Euclidean Distance"
    JACCARD = "Jaccard Similarity (non-vectorized)"


class Result(BaseModel):
    value: float
    text1: str
    text2: str


class Input(BaseModel):
    text1: str = Field(max_length=3250)
    text2: str = Field(max_length=3250)
    vectorizing: VectorizingMethod
    similarity: SimilarityMethod

    def compare(self):
        texts = [i.lower().split(" ") for i in [self.text1, self.text2]]

        similarity_methods = {
            SimilarityMethod.COSINE: {
                VectorizingMethod.TFIDF: lambda: cosinus_similarity(*tfidf_vectorize(self.text1, self.text2)),
                VectorizingMethod.COUNT: lambda: cosinus_similarity(
                    *count_vectorize(self.text1, self.text2))
            },
            SimilarityMethod.EUCLID: {
                VectorizingMethod.TFIDF: lambda: euclidean_distance(*tfidf_vectorize(self.text1, self.text2)),
                VectorizingMethod.COUNT: lambda: euclidean_distance(
                    *count_vectorize(self.text1, self.text2))
            }
        }

        if self.similarity == SimilarityMethod.JACCARD:
            similarity = round(jaccard_similarity(texts[0], texts[1]), 2)
        else:
            similarity = similarity_methods[self.similarity][self.vectorizing](
            )

        return Result(value=similarity, text1=self.text1, text2=self.text2)
