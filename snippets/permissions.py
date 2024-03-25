from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """ 
    Custom permission that allows only owner to edit the object.
    """
    def has_object_permission(self, request, view, obj):
        # Read Permissions for everyone (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions for owner
        return obj.owner == request.user