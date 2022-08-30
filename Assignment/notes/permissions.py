from rest_framework import permissions


class SuperUserReadOnly(permissions.BasePermission):

    # edit_methods = ("GET","POST","PUT","PATCH")
    def has_permission(self, request, view):
        print("In permission")
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        print("request : ", request.user.is_superuser)
        if request.user.is_superuser:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False
