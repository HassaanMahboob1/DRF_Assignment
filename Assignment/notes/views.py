from django.shortcuts import render, HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.serializers import *
from rest_framework.response import Response
from .serializers import RegisterSerializer, NotesSerializer
from notes.models import User, Notes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from notes.filters import ArchiveFilter
from notes.permissions import SuperUserReadOnly
from django_filters import rest_framework as filters
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from django.core import serializers


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Notes.objects.all()

    def list(self, request):
        queryset = Notes.objects.all()
        user = request.user
        queryset = queryset.filter(user=user, archive=0)
        data = serializers.serialize("json", queryset)
        return HttpResponse(data, content_type="application/json")


class ArchiveViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('archive',)
    permission_classes = [
        SuperUserReadOnly,
    ]

    def list(self, request):
        queryset = Notes.objects.all()
        user = request.user
        queryset = queryset.filter(user=user, archive=1)
        data = serializers.serialize("json", queryset)
        return HttpResponse(data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        queryset = Notes.objects.all()
        queryset = queryset.filter(pk=kwargs["pk"])
        queryset.update(archive=1)
        data = serializers.serialize("json", queryset)
        return HttpResponse(data, content_type="application/json")


@api_view(["GET", "PATCH"])
def shared(request):
    queryset = Notes.objects.all()
    curr_user = request.user.id
    queryset = queryset.filter(sharedwith=curr_user)
    data = serializers.serialize("json", queryset)
    return HttpResponse(data, content_type="application/json")
