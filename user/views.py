from django.shortcuts import render
from rest_framework import viewsets, permissions

from user.models import User
from user.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet для пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
