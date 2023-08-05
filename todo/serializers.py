from .models import *
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response
import logging

# Get the logger for the current module
# logger = logging.getLogger(__name__)
# logger.info('This is an info message')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        current_user = self.context['request'].user
        validated_data['user'] = current_user
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.pop('title')
        instance.description = validated_data.pop('description')
        instance.due_date = validated_data.pop('due_date')
        instance.status = validated_data.pop('status')
        instance.priority = validated_data.pop('priority')
        instance.lable = validated_data.pop('lable')
        instance.save
        
        return instance