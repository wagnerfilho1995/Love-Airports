"""backend URL Configuration

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
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from core.routes import router as core_router
# from django.conf import settings
# from django.conf.urls.static import static

schema_view = get_swagger_view(title='LOVE AIRPORTS API')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('core/', include(core_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
