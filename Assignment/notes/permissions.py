from rest_framework import permissions


class SuperUserReadOnly(permissions.BasePermission):

    edit_methods = ("GET", "POST", "PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return False
            return True
