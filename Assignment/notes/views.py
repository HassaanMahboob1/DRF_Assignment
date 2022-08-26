from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import *
from .serializers import RegisterSerializer, NotesSerializer
from notes.models import User, Notes
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from django.core import serializers


# Class based view to register user
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
        queryset = queryset.filter(user=user)
        data = serializers.serialize("json", queryset)
        return HttpResponse(data, content_type="application/json")

    # def partial_update(self, request, *args, **kwargs):
    #     id = kwargs['pk']
    #     queryset = Notes.objects.all()
    #     user = request.user
    #     queryset = queryset.filter(user=user , id = id)
    #     print(queryset)
    #     data = serializers.serialize("json", queryset)
    #     return HttpResponse(data, content_type="application/json")
