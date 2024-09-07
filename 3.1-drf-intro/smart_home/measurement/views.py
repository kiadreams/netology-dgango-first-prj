from rest_framework import generics
from django.shortcuts import redirect, reverse

from measurement.models import Measurement, Sensor
from measurement import serializers


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
def index(request):
    return redirect(reverse('all_sensors'))


class MeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer


class SensorsView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorsSerializer


class SensorDataView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.select_related().all()
    serializer_class = serializers.SensorDetailSerializer
    lookup_field = 'id'
