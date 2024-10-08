"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from rest_framework.response import Response


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """API Root."""
    return Response({
        'docs': reverse('swagger-ui', request=request),
    })


apps_patterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('apps.user.urls')),
]

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),

    # Third party
    path('api-auth/', include('rest_framework.urls')),

    # API
    path('', api_root),
    path('api/v1/', include((apps_patterns, 'v1'), namespace='v1')),
    path('api/docs/', login_required(
        TemplateView.as_view(
            template_name='docs/swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
        )
    ), name='swagger-ui'),

    # Testing
    path('sentry-debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
