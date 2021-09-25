from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилюю'
        for field_name, field in self.fields.items():
           field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

    # Validators
    def clean_username(self):
        data = self.cleaned_data['username']
        if data[0].isdigit():
            raise forms.ValidationError('Имя пользователя не может начинаться с цифры')
        elif len(data) < 2:
            raise forms.ValidationError('Имя пользователя слишком короткое, рекомендуется сменить его на более длинное')
        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if data[0].isdigit():
            raise forms.ValidationError('Имя не может начинаться с цифры')
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if data[0].isdigit():
            raise forms.ValidationError('Фамилия не может начинаться с цифры')
        return data


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите эл. почту'
        self.fields['age'].widget.attrs['placeholder'] = 'Введите возраст'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
