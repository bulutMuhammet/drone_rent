from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Kullanıcı yönetici ise veya isteği yapan kullanıcı sahip ise izin ver
        return request.user.is_superuser or obj.renting_user == request.user


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Kullanıcı yönetici ise izin ver
        return request.user.is_superuser
