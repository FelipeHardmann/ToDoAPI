from app.models import ToDo
from rest_framework import serializers

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'name', 'done', 'created_at']
