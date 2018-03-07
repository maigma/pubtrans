from rest_framework import serializers
from .models import AppStopsModel

class AppStopsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppStopsModel
        fields = '__all__'
