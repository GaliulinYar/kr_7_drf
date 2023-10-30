from django.shortcuts import render
from rest_framework import generics, permissions

from main.models import Habit
from main.pagination import HabitPaginator
from main.serializers import HabitSerializer, HabitCreateSerializer


# Create your views here.

class HabitListAPIView(generics.ListAPIView):
    """generic для вывода списка привычек других пользователей публичность True"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator  # Пагинация для вывода по 5 привычек
    queryset = Habit.objects.filter(is_public=True)


class MyHabitListAPIView(generics.ListAPIView):
    """generic для вывода списка привычек текущего пользователя"""
    serializer_class = HabitSerializer  # определяем сериализатор
    pagination_class = HabitPaginator  # Пагинация для вывода по 5 привычек
    permission_classes = [permissions.IsAuthenticated]  # подмешиваем авторизацию через токен API

    def get_queryset(self):
        if self.request.user.is_authenticated:  # проверка на аудентификацию пользователя
            return Habit.objects.filter(owner=self.request.user)  # фильтруем привычки пользователя
        return Habit.objects.none()


class HabitCreateAPIView(generics.CreateAPIView):
    """generic для создания списка привычек пользователей"""
    serializer_class = HabitCreateSerializer  # определяем сериализатор


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Generic для обновления урока Lesson"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:  # проверка на аудентификацию пользователя
            return Habit.objects.filter(owner=self.request.user)  # фильтруем привычки пользователя
        return Habit.objects.none()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """generic для удаления привычки пользователем"""
    serializer_class = HabitCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:  # проверка на аудентификацию пользователя
            return Habit.objects.filter(owner=self.request.user)  # фильтруем привычки пользователя
        return Habit.objects.none()
