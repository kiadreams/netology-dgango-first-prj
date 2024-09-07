from rest_framework import serializers

from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы
class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
