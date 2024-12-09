from django.urls import path

from . import views

app_name = 'dashboard'  # name space for this app

urlpatterns = [
    path('', views.index, name='index')
]
