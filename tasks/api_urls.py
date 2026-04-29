from django.urls import path
from . import api_views

urlpatterns = [
    path('tasks/', api_views.TaskListAPI.as_view(), name='api_task_list'),
    path('tasks/<int:task_id>/', api_views.TaskDetailAPI.as_view(), name='api_task_detail'),
    path('tasks/<int:task_id>/toggle', api_views.TaskToggleAPI.as_view(), name='api_task_toggle')
]