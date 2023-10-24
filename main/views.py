from django.shortcuts import render
from rest_framework import generics

from main.models import Habit
from main.pagination import HabitPaginator
from main.serializers import HabitSerializer


# Create your views here.

class HabitListAPIView(generics.ListAPIView):
    """generic для вывода списка привычек других пользователей публичность True"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator  # Пагинация для вывода по 5 привычек
    queryset = Habit.objects.filter(is_public=True)


class HabitCreateAPIView(generics.CreateAPIView):
    """generic для вывода списка привычек других пользователей"""
