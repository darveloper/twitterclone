"""twitterclone URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from twitter import views
from twitteruser.views import (
    registration_view,
    logout_view,
    login_view,
    must_authenticate_view,
    account_view,
    Profile,
    ProfileFollowToggle,
    
    
)

app_name = 'twitteruser'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('account/', account_view, name='account'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('must_authenticate/', must_authenticate_view, name='must_authenticate'),
    path('register/', registration_view, name='register'),
    path('tweet/', include('tweet.urls', 'tweet')),
    url(r'^user/(?P<username>[A-Za-z0-9]+)/$', Profile, name='profile'),
    url(r'^follow/$', ProfileFollowToggle.as_view(), name='follow'),
    
    
    
    
]

