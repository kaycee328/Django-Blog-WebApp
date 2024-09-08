from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ChangePassword
from .models import Profile
from django.views.generic import DetailView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetDoneView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for "{username}", login here!')
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "uform": u_form,
        "pform": p_form,
    }
    return render(request, "users/profile.html", context)


class Login_user(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy("blog-home")


class Logout_user(LogoutView):
    template_name = "users/logout.html"


# class Reset_Password_View(PasswordResetView):
#     template_name = 'users/password_reset.html'
#     success_url = reverse_lazy('password_reset_confirm')

# class Password_Reset_Confirm(PasswordResetConfirmView):
#     template_name = 'password_reset_confirm.html',
#     success_url = reverse_lazy('reset_password_done')


# class Reset_Password_Done_View(PasswordResetDoneView):
#     template_name = 'password_reset_done.html'

# class Reset_Password_Complete(PasswordResetCompleteView):
#     template_name = 'password_reset_done.html'
