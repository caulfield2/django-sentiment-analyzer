from django.db import models


class Analysis(models.Model):
    text = models.TextField()
    sentiment = models.DecimalField(max_digits=5, decimal_places=4)

    @classmethod
    def create(cls, text, sentiment):
        analysis = cls(text=text, sentiment=sentiment)
        return analysis
