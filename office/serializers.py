from rest_framework import serializers
from .models import Task, Employee

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate(self, data):
        assignee = data['assignee']
        assigned_by = data['assigned_by']

        # Ensure that assignee is always a Lead and assigned_by is always a Subordinate
        if assignee.role != 'Lead':
            raise serializers.ValidationError({'assignee': 'The assignee must be a Lead.'})
        if assigned_by.role != 'Subordinate':
            raise serializers.ValidationError({'assigned_by': 'The assigned_by must be a Subordinate.'})

        return data

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'