from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "instructor"
        )
    
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "student" and
            request.method in SAFE_METHODS
        )