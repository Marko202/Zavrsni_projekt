from django.urls import path
from . import views
from myapp.views import ProductList, ProfileList, SellerProductList

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('seller/<str:seller>/', SellerProductList.as_view(), name='seller_products'),
    
    path('profiles/', views.ProfileListView.as_view(), name='profile_list'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),

    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),

    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),

    path('messages/', views.MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
]