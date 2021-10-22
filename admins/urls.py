from django.contrib import admin
from django.urls import path
from admins.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    CategoriesListView, ProductsListView, CategoriesCreateView, ProductsCreateView, ProductsDeleteView, \
    ProductsUpdateView, CategoriesUpdateView, CategoriesDeleteView, admin_users_recover

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('user-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('user-recover/<int:id>', admin_users_recover, name='admin_users_recover'),
    path('admin-categories/', CategoriesListView.as_view(), name='admin_categories'),
    path('admin-categories-create/', CategoriesCreateView.as_view(), name='admin_categories_create'),
    path('categories-update/<int:pk>', CategoriesUpdateView.as_view(), name='admin_categories_update'),
    path('categories-delete/<int:pk>', CategoriesDeleteView.as_view(), name='admin_categories_delete'),
    path('admin-products/', ProductsListView.as_view(), name='admin_products'),
    path('admin-products-create/', ProductsCreateView.as_view(), name='admin_products_create'),
    path('product-update/<int:pk>', ProductsUpdateView.as_view(), name='admin_products_update'),
    path('product-delete/<int:pk>', ProductsDeleteView.as_view(), name='admin_products_delete'),
]
