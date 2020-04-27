"""sunnyville URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^search/', include('haystack.urls'), name="haystack_search"),
    url(r'^', include('blog.urls', namespace='posts')),
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'),permanent=False), name="favicon"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
