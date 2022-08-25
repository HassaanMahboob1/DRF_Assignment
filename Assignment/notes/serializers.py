from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User, Notes
from datetime import date


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    username = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data):
        user_obj = User.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            username=validated_data["username"],
            last_name=validated_data["last_name"],
        )
        user_obj.set_password(validated_data["password"])
        user_obj.save()
        return user_obj


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

    def create(self, validated_date):
        note = Notes.objects.create(
            text=validated_date["text"],
            date_created=date.today(),
            date_updated=date.today(),
            user=self.context["request"].user,
        )

        note.save()
        return note
