from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers

# Create your views here.
