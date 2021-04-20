from django.conf.urls import url
from product import views
from django.urls import path,include


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('product/new/', views.CreateProductView.as_view(), name='product_new'),
    path('product/<int:pk>/edit', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/remove', views.ProductDeleteView.as_view(), name='product_remove'),
]