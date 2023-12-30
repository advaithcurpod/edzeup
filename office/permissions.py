from rest_framework import permissions

class CanAssignTaskPermission(permissions.BasePermission):
    message = "You do not have permission to assign tasks."

    def has_permission(self, request, view):
        # Check if the user belongs to the Lead group
        return request.user.groups.filter(name='Lead').exists()

    def has_object_permission(self, request, view, obj):
        # Check if the user belongs to the Lead group and the task is assigned to a subordinate
        return request.user.groups.filter(name='Lead').exists() and obj.assignee.groups.filter(name='Subordinate').exists()