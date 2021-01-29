from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galeria/', views.galeria, name='galeria'),
    path('cotizar/', views.cotizar, name='cotizar'),
    path('categoria/', views.categoria, name='categoria'),
    path('somos/', views.somos, name='somos'),
]