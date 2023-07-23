from .models import *
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response


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

        # user = validated_data['user']
        # if current_user != user:
        #     raise serializers.ValidationError(
        #         detail="only current login user can create todo.",
        #         code=412)

        return Todo.objects.create(**validated_data)
