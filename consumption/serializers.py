from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import days, months


class DayDataSerializer(serializers.Serializer):
    data = serializers.SerializerMethodField('data_list')

    def data_list(self, data):
        return ([data.timestamp, data.consumption, data.temperature])

    class Meta:
        model = days
        fields = ['timestamp', 'consumption', 'temperature', 'data']


class MonthDataSerializer(ModelSerializer):
    class Meta:
        model = months
        fields = [
            'timestamp',
            'consumption',
            'temperature',
        ]
