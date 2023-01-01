from django.urls import path, include
from .views import CustomObtainTokenPairView, AuthViewSets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', AuthViewSets, basename="accounts")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomObtainTokenPairView.as_view(), name='login'),
]
