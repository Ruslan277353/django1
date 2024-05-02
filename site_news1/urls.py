"""
URL configuration for site_news1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from news.views import home_page, MyFormView, search_news, single_new, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('search', search_news, name='search_new'),
    path('new/<int:id>', single_new),
    path('register', MyFormView.as_view()),
    path('login/', login_view, name='login')
]
