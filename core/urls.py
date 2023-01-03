from django.contrib import admin
from django.urls import path, include
from account.views import CustomObtainTokenPairView, AuthViewSets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/users/login/', CustomObtainTokenPairView.as_view(), name='login'),
    path('api/auth/', include('account.urls')),


]
