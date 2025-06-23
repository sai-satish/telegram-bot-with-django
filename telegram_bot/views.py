from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .accounts_forms import RegisterForm, LoginForm
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from celery_setup.background_task import send_email_helper

def redirect_to_home(request):
    return redirect('home/')

def home_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.COOKIES.get("is_authenticated") == "true":
        return redirect("Home")
    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = redirect('Home')  # or dashboard
            response.set_cookie(
                key='jwt',
                value=access_token,
                httponly=True,
                secure=False,  # Set True in production with HTTPS
                samesite='Lax'
            )
            response.set_cookie('is_authenticated', 'true')

            return response
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "login.html", {"form": form})

def logout_view(request):
    # logout(request)
    response = redirect('Login')
    response.delete_cookie('jwt')
    response.delete_cookie('is_authenticated')
    return response

def register_view(request):
    if request.COOKIES.get("is_authenticated") == "true":
        return redirect("Home")

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        send_email_helper.delay([form.cleaned_data.get('email')])
        return redirect('Home')

    return render(request, 'register.html', {'form': form})


def contact_view(request):
    if request.COOKIES.get("is_authenticated") == "true":
        return redirect("https://www.t.me/Little983_bot")
    return redirect("Login")





