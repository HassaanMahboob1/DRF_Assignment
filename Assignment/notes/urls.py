from django.urls import path
from . import views
from .views import RegisterUserAPIView, NotesViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Notes", NotesViewSet, basename="Notes")


urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
    # path("notes/create", NotesAPIView.as_view()),
    # path("notes/show", NotesAPIView.as_view()),
] + router.urls
