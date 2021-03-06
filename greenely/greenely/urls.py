"""greenely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_jwt.views import verify_jwt_token
from rest_framework_swagger.views import get_swagger_view
from .default_values import (AUTH_API_URL, CONSUMPTION_API_URL,
                             SWAGGER_API_URL)

schema_view = get_swagger_view(title='greenely API')
urlpatterns = [
    url(AUTH_API_URL, include('authentication.urls')),
    url(CONSUMPTION_API_URL, include('consumption.urls')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(SWAGGER_API_URL, schema_view)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
