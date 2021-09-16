from django import forms

from products.models import ProductsCategory, Product
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class CategoryForm(forms.ModelForm):
    def __str__(self):
        return self.name


class CategoryCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductsCategory
        fields = ('name', 'description')

    def __str__(self):
        return self.name


class ProductForm(forms.ModelForm):
    def __str__(self):
        return f'{self.name} | {self.category}'


class ProductCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input',
                                                           }), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    category = forms.ChoiceField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4',
                                                             'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4',
                                                            'readonly': True}))
