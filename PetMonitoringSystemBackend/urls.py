"""PetMonitoringSystemBackend URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.views import serve

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView


def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure=True, **kwargs)


schema_view = get_schema_view(
    openapi.Info(
        title="Pet Monitoring Backend API",
        default_version='v1',
        description="Pet Monitoring Backend Swagger API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cxz123499@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('api.urls')),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  path('health/', include('health_check.urls')),
                  re_path(r'^static/(?P<path>.*)$', return_static, name='static'),

                  path('graphql/', GraphQLView.as_view(graphiql=True)),
                  
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
