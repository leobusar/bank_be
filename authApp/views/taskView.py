from rest_framework import status, viewsets
from authApp import serializers
from authApp.models import Task
from authApp.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        serializer = TaskSerializer(self.queryset.order_by("-due_date").filter(owner=9), many=True)
        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        serializer = TaskSerializer(task)
        return Response({'data': serializer.data})

    def update(self, request, pk=None):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response({'status': 'success'})
