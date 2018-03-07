from rest_framework import serializers
from .models import AppStopsModel

class AppStopsSerializer(serializers.ModelSerializer):

	COERCE_DECIMAL_TO_STRING = False

    class Meta:
        model = AppStopsModel
        fields = '__all__'
