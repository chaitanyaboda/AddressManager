from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
