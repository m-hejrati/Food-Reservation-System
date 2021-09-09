"""food_reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from web import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users/?$', views.UserViewSet)
router.register(r'menus/?', views.MenuViewSet, basename='menus')
router.register(r'orders/?', views.OrderViewSet)

urlpatterns = [
    path('admin', RedirectView.as_view(url = '/admin/')),
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include(router.urls)),
    url(r'^orders/add/?$', views.reserve),
    url(r'^orders/delete/?$', views.remove)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
