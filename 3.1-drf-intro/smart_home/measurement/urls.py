from django.urls import path

from measurement import views

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', views.SensorsView.as_view(), name='all_sensors'),
    path('sensors/<int:id>/', views.SensorDataView.as_view()),
    path('measurements/', views.MeasurementView.as_view()),
]
