from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    model = Task
    fields = ['id', 'body', 'status', 'date_time_created', 'date_time_modified']