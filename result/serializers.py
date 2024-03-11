from .models import Tracked, ConfigParameter, StreamPhoto
from rest_framework import serializers


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tracked
        fields = '__all__'


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigParameter
        fields = '__all__'


class StreamPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPhoto
        fields = '__all__'