from django import forms

from products.models import ProductsCategory, Product
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class CategoryAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')


class ProductAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False)
    price = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control py-4"}), required=False)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    category = forms.ModelChoiceField(widget=forms.Select, queryset=ProductsCategory.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
