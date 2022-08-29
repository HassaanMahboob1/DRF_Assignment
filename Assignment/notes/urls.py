from django.urls import path
from . import views
from .views import RegisterUserAPIView, NotesViewSet, archivelist, shared
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Notes", NotesViewSet, basename="Notes")


urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
    path("archive/<id>", views.archive, name="archive"),
    path("archive/", views.archivelist, name="archivelist"),
    path("shared", views.shared, name="shared"),
] + router.urls
