from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('aceleracion/', views.aceleracion, name='aceleracion'),
    path ('posicion/', views.posicion, name='posicion'),
]