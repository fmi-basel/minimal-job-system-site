"""job_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login,{'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'core/logout.html', 'next_page': '/login'}, name='logout'),
    url(r'^change-password/', auth_views.PasswordChangeView.as_view(success_url='/frontend'), name='change_password'),
    # url(r'^admin/', ExtendedAdminSite.get_urls),
    url(r'^$', lambda r: HttpResponseRedirect('frontend/')),
    url(r'^api/', include('job_system_api.urls')),
    url(r'^frontend/', include('job_system_frontend.urls'))
]
