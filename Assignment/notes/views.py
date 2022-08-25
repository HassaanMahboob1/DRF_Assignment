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

from django.core import serializers


# Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class NotesAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotesSerializer

    def get(self, request):
        queryset = Notes.objects.all()
        user = request.user
        queryset = queryset.filter(user=user)
        data = serializers.serialize("json", queryset)
        return HttpResponse(data, content_type="application/json")

    # def put(self, request, pk, format=None):
    #   snippet = self.get_object(pk)
    #   serializer = SnippetSerializer(snippet, data=request.DATA)
    #   if serializer.is_valid():
    #       serializer.save()
    #       return Response(serializer.data)
    #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return HttpResponse("Object has deleted")
