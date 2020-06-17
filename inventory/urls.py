from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('create-product/', views.create_product, name="create-product"),
    path('edit-product/<str:pk>/', views.edit_product, name="edit-product"),
    path('delete-product/<str:pk>/', views.delete_product, name="delete-product"),
]