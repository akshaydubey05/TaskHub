from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer

class CreateTaskView(generics.CreateAPIView):
    """Create a new task"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AssignTaskView(APIView):
    """Assign task to users"""
    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            user_ids = request.data.get('user_ids', [])
            users = User.objects.filter(id__in=user_ids)
            task.assigned_users.set(users)
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

class UserTasksView(generics.ListAPIView):
    """Get all tasks for a specific user"""
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)