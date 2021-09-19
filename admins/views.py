from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminForm, CategoryAdminForm
from users.models import User
from products.models import ProductsCategory, Product


# Create your views here.

def index(request):
    return render(request, 'admins/admin.html')


# Категории
class CategoriesListView(ListView):
    model = ProductsCategory
    context_object_name = 'categories'
    template_name = 'admins/admin-categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории товаров'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesListView, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == "POST":
        form = CategoryAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoryAdminForm()
    context = {
        'title': 'GeekShop - Админ | Создание категории',
        'form': form
    }
    return render(request, 'admins/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, id):
    categories_select = ProductsCategory.objects.get(id=id)
    if request.method == "POST":
        form = CategoryAdminForm(data=request.POST, instance=categories_select, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно изменена')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoryAdminForm(instance=categories_select)
    context = {
        'title': 'GeekShop - Админ | Редактирование категории',
        'form': form,
        'categories_select': categories_select
    }

    return render(request, 'admins/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, id):
    category = ProductsCategory.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('admins:admin_categories'))


# Товары
class ProductsListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'admins/admin-products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Продукты'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsListView, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == "POST":
        form = ProductAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно добавлен')
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminForm()
    context = {
        'title': 'GeekShop - Админ | Создание продукта',
        'form': form
    }
    return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    products_select = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductAdminForm(data=request.POST, instance=products_select, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные продукта успешно изменены')
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminForm(instance=products_select)
    context = {
        'title': 'GeekShop - Админ | Редактирование продукта',
        'form': form,
        'products_select': products_select
    }

    return render(request, 'admins/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products'))


# Юзеры
class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == "POST":
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
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
            messages.success(request, 'Данные успешно изменены')
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


@user_passes_test(lambda u: u.is_superuser)
def admin_users_recover(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
