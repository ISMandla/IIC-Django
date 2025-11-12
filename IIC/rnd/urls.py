from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.rnd , name = "research"),
    path('department/<int:pk>', views.depart , name = "depart"),
    path('faculty/<int:pk>', views.facul , name = "facul"),

]
