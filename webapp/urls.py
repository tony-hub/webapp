"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from novel import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^search/$', views.search,name='search'),
    url(r'^sort/(?P<type>\d+)/(?P<novelid>\d+)/$', views.more,name='sort'),
    url(r'^content/(?P<novelid>\d+)/$', views.detail,name='content'),
    url(r'^chapter/(?P<chapterid>\d+)/$', views.chapter,name='chapter'),
]
