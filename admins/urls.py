from django.contrib import admin
from django.urls import path
from admins.views import index, UserListView, admin_users_create, admin_users_update, admin_users_delete, \
    CategoriesListView, ProductsListView, admin_categories_create, admin_products_create, admin_products_delete, \
    admin_products_update, admin_categories_update, admin_categories_delete, admin_users_recover

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', admin_users_create, name='admin_users_create'),
    path('user-update/<int:id>', admin_users_update, name='admin_users_update'),
    path('user-delete/<int:id>', admin_users_delete, name='admin_users_delete'),
    path('user-recover/<int:id>', admin_users_recover, name='admin_users_recover'),
    path('admin-categories/', CategoriesListView.as_view(), name='admin_categories'),
    path('admin-categories-create/', admin_categories_create, name='admin_categories_create'),
    path('categories-update/<int:id>', admin_categories_update, name='admin_categories_update'),
    path('categories-delete/<int:id>', admin_categories_delete, name='admin_categories_delete'),
    path('admin-products/', ProductsListView.as_view(), name='admin_products'),
    path('admin-products-create/', admin_products_create, name='admin_products_create'),
    path('product-update/<int:id>', admin_products_update, name='admin_products_update'),
    path('product-delete/<int:id>', admin_products_delete, name='admin_products_delete'),
]
