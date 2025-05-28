"""
URL configuration for djangoLogin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from posteos.views import AdminStatsView # Importar la vista de estadísticas

urlpatterns = [
    path("admin/stats/", AdminStatsView.as_view(), name="admin_stats"), # URL para estadísticas de administración
    path("admin/", admin.site.urls),
    path("", include("posteos.urls")), # Incluye las URLs de la aplicación posteos
    path("accounts/", include("django.contrib.auth.urls")), # Incluye las URLs de autenticación de Django
]
