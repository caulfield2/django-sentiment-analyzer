from django.shortcuts import render
from django.http import HttpResponse

def analyze(request):
    return HttpResponse('Sentiment analysis')
