"""
URL configuration for telegram_bot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_view, register_view, login_view, contact_view, redirect_to_home, logout_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('', redirect_to_home),
    path('home/', home_view, name="Home"),
    path('register/', register_view, name="Register"),
    path('login/', login_view, name ="Login"),
    # path('login/', TokenObtainPairView.as_view(), name='Login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('contact/', contact_view, name = "Contact"),
    path('logout/', logout_view, name='Logout'),
    path('admin/', admin.site.urls),
]
