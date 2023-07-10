from app.models import ToDo
from app.serializers import ToDoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


class ToDoListAndCreate(APIView):
    def get(self, request):
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetailChangeAndView(APIView):
    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)
    
    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        

