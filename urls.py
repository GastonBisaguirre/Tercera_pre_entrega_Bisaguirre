from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto_Bisaguirre/', include('proyecto_Bisaguirre.urls')),
]
