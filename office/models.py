# office/models.py
from django.db import models
from user.models import User
from django.core.exceptions import ValidationError

class Task(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_by_tasks')

    def __str__(self):
        return self.title
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, related_name='employees')

    def __str__(self):
        return self.user.username
