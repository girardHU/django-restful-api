from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.ModelSerializer):
    todo_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'todo_set']

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ["id", "task", "completed", "timestamp", "updated", "owner"]
