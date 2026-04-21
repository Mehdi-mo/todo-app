from django.urls import path
from .import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks_list'),
    path("task/<int:task_id>/edit/", views.task_edit, name="task_edit"),
    path('task/<int:task_id>/toggle/', views.task_toggle, name='task_toggle'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete')
]
