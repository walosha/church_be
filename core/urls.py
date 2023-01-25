from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from account.views import CustomObtainTokenPairView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/users/login/', CustomObtainTokenPairView.as_view(), name='login'),
    path('api/auth/', include('account.urls')),
    path('api/polls/', include('poll.urls')),
    path('api/attendances/', include('attendance.urls')),
    path('api/messages/', include('message.urls')),
    path('api/events/', include('event.urls')),
    path('api/blogs/', include('blog.urls')),
    path('api/siteinfo/', include('siteinfo.urls')),
    path('api/podcast/', include('podcast.urls')),
    path('api/giving/', include('giving.urls')),
    # Optional UI:
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
