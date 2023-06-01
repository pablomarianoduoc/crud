from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('registrarAlumno/', views.registrarAlumno),
    path('eliminacionAlumno/<rut>', views.eliminacionAlumno),
]