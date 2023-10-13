from rest_framework import serializers
from api.models import Task


class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'