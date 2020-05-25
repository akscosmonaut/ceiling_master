from django.contrib import admin
from django.urls import path
from dipapp import views

urlpatterns = [
    path('index', views.index),
    path('', views.index),
    path('create/', views.create),
    path('ceiling_kind', views.ceiling_kind),
    path('gallery', views.gallery),
    path('review', views.review),
    path('advice', views.advice),
    path('price', views.review),
    path('admin/', admin.site.urls),
]