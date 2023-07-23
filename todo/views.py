from django.shortcuts import render
from rest_framework import viewsets, permissions,status


from .models import *
from .serializers import *
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication, SessionAuthentication


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class Show_User(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = CustomPagination
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        return Response("method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)


class Show_Todo(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    pagination_class = CustomPagination
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        todos = Todo.objects.filter(user_id=user.id)
        serializer=TodoSerializer(data=todos,many=True)
        serializer.is_valid()
        return Response(serializer.data)
