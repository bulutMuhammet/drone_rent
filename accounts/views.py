from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import UserRegistrationForm


class LoginView(LoginView):
    template_name = 'auth/login.html'  # Kullanıcı giriş formunun görüntüleneceği şablon
    success_url = reverse_lazy('index')  # Başarılı giriş sonrası yönlendirilecek URL

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(*args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, "Geçersiz eposta veya şifre.")
        return super().form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)


class LogoutView(LogoutView):
    next_page = reverse_lazy(
        'login')


class RegisterView(FormView):
    template_name = 'auth/register.html'  # Kayıt formunun görüntüleneceği şablon
    form_class = UserRegistrationForm  # Özel kullanıcı kayıt formu
    success_url = reverse_lazy(
        'login')  # Başarılı kayıt sonrası yönlendirilecek URL

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(*args, **kwargs)

    # eğer form geçerliyse çalışacak fonksiyon
    def form_valid(self, form):
        form.save(commit=False)
        user = form.instance
        user.username = user.email # kullanıcın username ve email alanlarını aynı yapıyorum
        user.save()
        messages.success(self.request,
                         "Başarıyla kayıt oldunuz. Şimdi giriş yapabilirsiniz")

        return super().form_valid(form)


