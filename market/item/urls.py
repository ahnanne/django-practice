from django.urls import path

from . import views

app_name = 'item'  # name space for this app

urlpatterns = [
    path('new/', views.new, name='new'),
    path('category/<int:category_id>/', views.category, name='category'),
    path(
        '<int:pk>/',  # integer, primary key
        views.detail,
        name='detail'
    ),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/edit', views.edit, name='edit'),
]
