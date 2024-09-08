from rest_framework import generics
from django.shortcuts import redirect, reverse
from .models import Measurement, Sensor
from . import serializers


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

    def patch(self, request, *args, **kwargs):
        self.serializer_class = serializers.SensorInfoSerializer
        return super().patch(request, *args, **kwargs)
