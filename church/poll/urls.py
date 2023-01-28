from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSets, PollCategoryCreateListAPIView  # QuestionViewSets

app_name = 'poll'

router = DefaultRouter()
router.register('', PollViewSets)
# router.register("", PollCategoryCreateListAPIView.as_view(),
#                 basename="category_listcreate")


urlpatterns = [
    path('', include(router.urls)),
]
