from django import forms

from products.models import ProductsCategory, Product
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class CategoryAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}), required=False)
    # is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-control py-4"}))
    discount = forms.IntegerField(widget=forms.NumberInput(), label='скидка', required=False, min_value=0, max_value=90,
                                  initial=0)

    class Meta:
        model = ProductsCategory
        fields = ('name', 'description', 'discount')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ProductAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput(), required=False)
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    price = forms.DecimalField(widget=forms.TextInput(), required=False)
    quantity = forms.IntegerField(widget=forms.TextInput())
    category = forms.ModelChoiceField(widget=forms.Select, queryset=ProductsCategory.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
