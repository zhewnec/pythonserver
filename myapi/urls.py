# _*_ coding:utf-8 _*_
"""myapi URL Configuration

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
from django.views import static
from django.conf import settings
from . import view, testdb
from django.contrib import admin
from caad import dispatcher
urlpatterns = [
    url(r'^$', view.index),
    url(r'^admin/', admin.site.urls),
    url(r'^testdb', testdb.testdb),

    # url(r'^sonar/', view.soanr),
    url(r'^report$', view.report),
    url(r'^CheckReport', view.CheckReport),
    url(r'^FormalReport', view.FormalReport),
    url(r'^TestrePort', view.TestrePort),
    url(r'^jenkinsapi', view.jenkinsapi),
    url(r'^dispathapi', dispatcher.dispathapi),
    url(r'^search', dispatcher.search),
    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

]
handler404 = view.page_not_found
