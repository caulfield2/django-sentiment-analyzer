import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .models import Analysis

nltk.download("vader_lexicon")
analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text):
    sentiment = analyzer.polarity_scores(text)["compound"]
    return Analysis.create(text=text, sentiment=sentiment)
