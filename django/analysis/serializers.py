from rest_framework import serializers
from .models import Analysis


class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = ["text", "sentiment"]
        read_only_fields = ["sentiment"]
