from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AnalysisSerializer
from analysis.utils import get_sentiment


class AnalysisViewSet(viewsets.ModelViewSet):
    serializer_class = AnalysisSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        text = request.data.get("text")
        instance = get_sentiment(text)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
