"""QRCodeGenerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from Generator.views import GenerateQRCodeView
from Website.views import (QRCodeView,
                           HomeView,
                           TopQRCodesView,
                           LatestQRCodesView,
                           AboutView,
                           SignUpView,
                           AccountView,
                           ChangePasswordView,
                           LogoutView)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('generate-qrcode/', GenerateQRCodeView.as_view(), name='generate-qrcode'),
    path('qrcode/<str:name_id>/', QRCodeView.as_view(), name='qrcode-view'),
    path('latest/', LatestQRCodesView.as_view(), name='latest-qrcodes'),
    path('top/', TopQRCodesView.as_view(), name='top-qrcodes'),
    path('about/', AboutView.as_view(), name='about'),
    path('account/', AccountView.as_view(), name='account'),
    path('account/password/', ChangePasswordView.as_view(), name='account-password'),
    path('signup/', SignUpView.as_view(), name='sign-up'),

    # Auth
    # ----
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
