"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admins.views import index, admin_users, admin_users_create, admin_users_update, admin_users_delete, \
    admin_categories, admin_products, admin_categories_create, admin_products_create, admin_products_delete, \
    admin_products_update, admin_categories_update, admin_categories_delete, admin_users_recover

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('user-create/', admin_users_create, name='admin_users_create'),
    path('user-update/<int:id>', admin_users_update, name='admin_users_update'),
    path('user-delete/<int:id>', admin_users_delete, name='admin_users_delete'),
    path('user-recover/<int:id>', admin_users_recover, name='admin_users_recover'),
    path('admin-categories/', admin_categories, name='admin_categories'),
    path('admin-categories-create/', admin_categories_create, name='admin_categories_create'),
    path('categories-update/<int:id>', admin_categories_update, name='admin_categories_update'),
    path('categories-delete/<int:id>', admin_categories_delete, name='admin_categories_delete'),
    path('admin-products/', admin_products, name='admin_products'),
    path('admin-products-create/', admin_products_create, name='admin_products_create'),
    path('product-update/<int:id>', admin_products_update, name='admin_products_update'),
    path('product-delete/<int:id>', admin_products_delete, name='admin_products_delete'),
]
