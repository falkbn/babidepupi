# encoding:utf-8

from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
    path('', views.index),
    path('populate/', views.populate_db_view),
    path('loadRS', views.load_rs),
    path('recommendedPeripheralsItems', views.recommended_peripheral_items),
    path('recommendedPeripheralsUser', views.recommended_peripheral_user),
    path('similarPeripherals', views.similar_peripherals),
    path('recommendedUsersPeripherals', views.recommended_users_peripherals),
    path('search', views.search),
    path('admin/', admin.site.urls),
]
