from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateForm, ProductCreateForm
from users.models import User
from products.models import ProductsCategory, Product


# Create your views here.

def index(request):
    return render(request, 'admins/admin.html')


# Категории
@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'categories': ProductsCategory.objects.all()
    }
    return render(request, 'admins/admin-categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == "POST":
        form = CategoryCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно саздана')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoryCreateForm()
    context = {
        'title': 'GeekShop - Админ | Создание категории',
        'form': form
    }
    return render(request, 'admins/admin-categories-create.html', context)


# Товары
@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == "POST":
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно добавлен')
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductCreateForm()
    context = {
        'title': 'GeekShop - Админ | Создание продукта',
        'form': form
    }
    return render(request, 'admins/admin-products-create.html', context)


# Юзеры
@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == "POST":
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'GeekShop - Админ | Регистрация',
        'form': form
    }

    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    users_select = User.objects.get(id=id)
    if request.method == "POST":
        form = UserAdminProfileForm(data=request.POST, instance=users_select, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Данные успешно изменены')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=users_select)
    context = {
        'title': 'GeekShop - Админ | Редактирование пользоваеля',
        'form': form,
        'users_select': users_select
    }

    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
