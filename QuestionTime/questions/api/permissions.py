from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    * Everyone can use safe methods ('GET', 'HEAD', 'OPTIONS')
    * Users can write data (create, update, ecc..) only for their own Question instances.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
