"""historial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


from django.conf.urls import url,include
from src import views
from src.views import ObjetivoCreateView, ObjetivoUpdateView, ObjetivoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ObjetivoCreateView.as_view(), name='index'),
    path('objetivo/<int:pk>/delete', ObjetivoDeleteView.as_view(), name='delete_objetivo'),
    path('objetivo/<int:objetivo_id>', ObjetivoUpdateView.as_view(), name='update_objetivo'),
]
