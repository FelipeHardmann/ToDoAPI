from app.models import ToDo
from app.serializers import ToDoSerializer

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from rest_framework.response import Response


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
