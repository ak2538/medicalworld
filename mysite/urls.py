from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('medicalworld/', include('medicalworld.urls')),
    path('admin/', admin.site.urls),
]