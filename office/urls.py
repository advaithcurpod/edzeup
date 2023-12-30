from django.urls import path
from .views import TaskListCreateView, TaskListView, EmployeeTaskDetailView

urlpatterns = [
    # post
    path('tasks/create/', TaskListCreateView.as_view(), name='task-list-create'),

    # get
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('<str:username>/', EmployeeTaskDetailView.as_view(), name='employee-task-details'),
]