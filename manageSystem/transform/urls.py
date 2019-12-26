from django.conf.urls import url, include
from .views import index, response_temp



urlpatterns = [
    url(r'^index', index, name='index'),
    url(r'^response/temp', response_temp, name='temp')
]