from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wipe/', views.wipe, name='wipe'),
    path('format/', views.format_view, name='format'),
]