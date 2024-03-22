from rest_framework.serializers import ModelSerializer
from .models import TodoModel

class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'description', 'created_at', 'due_date', 'status']