from django.urls import path
from .import views_1, views_2

urlpatterns = [
    path('', views_1.maps, name='maps'),
    path('views/', views_2.views, name='views')
]
