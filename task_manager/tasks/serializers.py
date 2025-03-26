from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)
    assigned_user_ids = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        write_only=True,
        source='assigned_users'
    )
    
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 
                 'status', 'completed_at', 'assigned_users', 'assigned_user_ids']