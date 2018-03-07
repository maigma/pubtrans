from rest_framework import serializers
from .models import AppStopsModel

class AppStopsSerializer(serializers.ModelSerializer):
    
    latitude = serializers.DecimalField(max_digits=8, decimal_places=6, coerce_to_string=False)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False)

    class Meta:
        model = AppStopsModel
        fields = '__all__'
