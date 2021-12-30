from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('categories/<int:category_id>/', views.merchandises),
    path('categories/<int:category_id>/merchandise/<int:merchandise_id>/', views.merchandise),
]

urlpatterns += [
    path('api/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/merchandises/', views.MerchandiseListCreateAPIView.as_view()),
    path('api/merchandises/<int:pk>/', views.MerchandiseRetrieveUpdateDestroyAPIView.as_view()),
    path('api/merchandise_pics/', views.MerchandiseIMGListCreateAPIView.as_view()),
    path('api/merchandise_pics/<int:pk>/', views.MerchandiseIMGRetrieveUpdateDestroyAPIView.as_view()),
]
