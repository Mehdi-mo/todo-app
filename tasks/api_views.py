from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskListAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        tasks = Task.objects.filter(user=request.user).order_by('-status','-datetime_created')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, task_id):
        task = Task.objects.get(id=task_id, user=request.user)
        serializer = TaskSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TaskToggleAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id, user=request.user)
        task.status = 'done' if task.status == 'pending' else 'pending'
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)