from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from account.views import CustomObtainTokenPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/users/login/', CustomObtainTokenPairView.as_view(), name='login'),
    path('api/auth/', include('account.urls')),
    path('api/attendances/', include('attendance.urls')),
    path('api/events/', include('event.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/doc/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
