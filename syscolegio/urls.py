"""
URL configuration for syscolegio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from syscolegio.views import inicio, estudiante, curso, saludo, saludo2, saludo3, html, html2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('academico.urls')),
    path('', inicio), #ruta de unicio
    path('estudiante/', estudiante),
    path('curso/', curso),
    path('saludo/<nombre>/<int:edad>', saludo),
    path('saludo2/<nombre>/<edad>', saludo2),
    path('saludo2/<nombre>', saludo3),
    path('html/', html),
    path('html2/', html2),
]