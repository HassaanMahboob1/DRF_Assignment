from django.urls import path
from . import views
from .views import RegisterUserAPIView, NotesAPIView

urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
    path("notes/create", NotesAPIView.as_view()),
    path("notes/show", NotesAPIView.as_view()),
]
