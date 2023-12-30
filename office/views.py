from rest_framework import generics, permissions, serializers
from .models import Task, Employee
from .serializers import TaskSerializer, EmployeeSerializer
from .permissions import CanAssignTaskPermission
from user.models import User

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [CanAssignTaskPermission]  # Apply the custom permission

    def perform_create(self, serializer):
        # Set task assigned by the current user who will be a Lead
        serializer.save(assigned_by=self.request.user)

        # Extract the username of the assignee from the request data
        assignee_username = self.request.data.get('assignee', None)
        title = self.request.data.get('title', None)
        deadline = self.request.data.get('deadline', None)

        if assignee_username and title and deadline:
            try:
                # Get the user object for the assignee
                assignee = User.objects.get(username=assignee_username)
                # Ensure that the assignee is a subordinate
                if assignee.role == 'Subordinate':
                    serializer.save(assignee=assignee)
                else:
                    # If the assignee is not a subordinate, delete the task and return an error response
                    serializer.instance.delete()
                    raise serializers.ValidationError({'assignee': 'The assignee must be a Subordinate.'})
            except User.DoesNotExist:
                # If the user with the provided username does not exist, delete the task and return an error response
                serializer.instance.delete()
                raise serializers.ValidationError({'assignee': 'User with the provided username does not exist.'})
        else:
            # If one of the fields is not provided, delete the task and return an error response
            serializer.instance.delete()
            raise serializers.ValidationError({'assignee': 'Assignee is required.',
                                                'title': 'Title is required.',
                                                'deadline': 'Deadline is required.'})
        
# list all the tasks assigned to the current user
class TaskListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

# list all tasks assigned to a particular employee whose username is provided in the URL
class EmployeeTaskDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
