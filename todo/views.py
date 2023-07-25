from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import viewsets, permissions, status

from .models import *
from .serializers import *
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


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

    def update(self, request, *args, **kwargs):
        return Response("method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response("method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)


class Show_Todo(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    pagination_class = CustomPagination
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'retrieve':
            pk = self.kwargs['pk']
            user = self.request.user
            try:
                queryset = Todo.objects.filter(user_id=user.id)
            except ObjectDoesNotExist:
                queryset = None
            return queryset




        if self.action == 'list':
            user = self.request.user
            queryset = Todo.objects.filter(user_id=user.id)
            return queryset
        return super().get_queryset()
