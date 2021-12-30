from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('categories/<int:category_id>/', views.merchandises),
    path('categories/<int:category_id>/merchandise/<int:merchandise_id>/', views.merchandise),
]