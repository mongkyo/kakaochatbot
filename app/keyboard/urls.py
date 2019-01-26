from django.urls import path
from . import views

app_name = 'keyboard'

urlpatterns = [
    path('', views.keyboard, name='keyboard'),
]
