from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Med', views.Med, name='Med'),
]