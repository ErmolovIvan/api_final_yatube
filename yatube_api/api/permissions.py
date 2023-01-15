from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    message = 'Нельзя изменять чужой контент!'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
