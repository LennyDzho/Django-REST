"""
URL configuration for WorkWithDRF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from rest_framework.routers import DefaultRouter



from demo.views import SensorListCreateView, SensorDetailView, TemperatureMeasurementCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Создание и получение списка датчиков
    path('sensors/', SensorListCreateView.as_view(), name='sensor_list_create'),

    # Получение полной информации по датчику и его изменение
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor_detail'),

    # Добавление измерения температуры
    path('measurements/', TemperatureMeasurementCreateView.as_view(), name='measurement_create'),
]

