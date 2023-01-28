from django.urls import path, include
from .views import AuthViewSets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', AuthViewSets, basename="accounts")

urlpatterns = router.urls
