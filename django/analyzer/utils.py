import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
analyzer = SentimentIntensityAnalyzer()


def get_articles():
    return {}


def get_sentiment(article):
    return analyzer.polarity_scores(article)
