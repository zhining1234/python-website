"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite.views import HomeView, UserCreateView, UserCreateDoneTV


urlpatterns = [
    # Admin 사이트
    path('admin/', admin.site.urls),
    
    # 계정 관리
    # https://github.com/django/django/blob/master/django/contrib/auth/urls.py
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'), 
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    # 어플리케이션
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('board/', include('board.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
