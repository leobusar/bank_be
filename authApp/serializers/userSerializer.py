from threading import activeCount
from authApp.models import User
from rest_framework import serializers
from .taskSerializer import TaskSerializer

class UserSerializer(serializers.ModelSerializer):
  tasks = TaskSerializer(many=True, read_only=True)
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'name', 'email', 'tasks']
