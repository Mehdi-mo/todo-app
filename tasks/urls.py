from django.urls import path
from .import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks_list'),
    path("task/<int:task_id>/edit/", views.TaskEditView.as_view(), name="task_edit"),
    path('task/<int:task_id>/toggle/', views.TaskToggleView.as_view(), name='task_toggle'),
    path('task/<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
