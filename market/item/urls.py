from django.urls import path

from . import views

app_name = 'item'  # name space for this app

urlpatterns = [
    path(
      '<int:pk>/',  # integer, primary key
      views.detail,
      name='detail'
    )
]
