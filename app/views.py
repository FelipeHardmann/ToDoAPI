from app.models import ToDo
from app.serializers import ToDoSerializer

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


class ToDoListAndCreate(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetailChangeAndView(generics.RetrieveUpdateDestroyAPIView):       
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
