from django.urls import path

from . import views

app_name = 'conversation'  # name space for this app

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
    path('inbox/', views.inbox, name='inbox'),
    path('detail/<int:conversation_pk>/', views.detail, name='detail'),
]
