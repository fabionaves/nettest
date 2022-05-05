"""nettest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from net.views import HostView, PingView, TipoListView, SnmpView, InterfaceView

urlpatterns = [
    path('', TipoListView.as_view(), name='index'),
    path('host/<int:pk>/interface/<str:interface>/', InterfaceView.as_view(), name='interface'),
    path('host/<int:pk>/', HostView.as_view(), name='host'),
    path('tipo/', TipoListView.as_view(), name='tipolist'),
    path('ping/<int:pk>/', PingView.as_view(), name='ping'),
    path('snmp/<int:pk>/', SnmpView.as_view(), name='snmp'),
    path('admin/', admin.site.urls),
]
