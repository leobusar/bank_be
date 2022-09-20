from django.db import models
from django.utils import timezone
from .user import User

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    due_date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)
