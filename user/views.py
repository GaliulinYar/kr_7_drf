from django.shortcuts import render
from rest_framework import viewsets

from user.models import User
from user.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet для пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def perform_create(self, serializer):
    #     """ Позволяем создавать и редактировать только свой профиль """
    #
    #     serializer.save(owner=self.request.user)
