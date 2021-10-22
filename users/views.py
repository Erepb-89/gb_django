from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy

from django.conf import settings

from django.core.mail import send_mail

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, UpdateView

from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm

# Create your views here.
from .models import User


class LoginListView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginListView, self).get_context_data()
        context['title'] = 'GeekShop - Авторизация'
        return context


class RegisterListView(SuccessMessageMixin, FormView):
    model = User
    template_name = 'users/register.html'
    success_message = 'Вы успешно зарегистрировались!'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(RegisterListView, self).get_context_data()
        context['title'] = 'GeekShop - Регистрация'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.success(request, 'Вы успешно зарегистрировались')
                return redirect(self.success_url)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})

    @staticmethod
    def send_verify_link(user):
        verify_link = reverse('users:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылке'
        message = f'Для подтверждения учетной записи {user.username} на портале GeekShop, пройдите по ссылке ' \
                  f'\n{settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    @staticmethod
    def verify(request, email, activation_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activation_key and not user.is_activation_key_expired():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users/verification.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('index'))


class ProfileFormView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    form_class_second = UserProfileEditForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Профиль'
        context['profile_form'] = self.form_class_second(instance=self.request.user.userprofile)
        return context

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        user = self.get_object()
        form = UserProfileForm(data=request.POST, instance=user, files=request.FILES)
        profile_form = UserProfileEditForm(data=request.POST, instance=user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            # messages.success(request, 'Данные успешно изменены')
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {
            'form': form,
            'profile_form': profile_form
        })


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))

class Logout(LogoutView):
    template_name = "products/index.html"
