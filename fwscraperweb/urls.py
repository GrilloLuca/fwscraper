from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls')),
    path('www/', include('www.urls')),
    path('admin/', admin.site.urls),
]
