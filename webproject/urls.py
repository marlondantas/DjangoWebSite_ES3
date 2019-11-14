from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('', include('candy.urls', namespace='CANDY')),
    path('admin/', admin.site.urls),
]
