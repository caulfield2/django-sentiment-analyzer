from django.shortcuts import render
from django.http import HttpResponse
from analyzer.utils import get_sentiment

def analyze(request):
    return HttpResponse(get_sentiment("This is a test of happy sentiment.")['compound'])
