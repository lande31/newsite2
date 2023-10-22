"""
URL configuration for newsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from . import settings
from users import views as user_view
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', user_view.register, name='register'),
    #path('', include('users.urls')),  path('login/', user_view.Login, name ='login'),
    path('login/', authentication_views.LoginView.as_view(template_name ='users/login.html'), name ='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name ='users/logout.html'), name ='logout'),
    path('profile/',user_view.profilepage, name= 'profile')
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
