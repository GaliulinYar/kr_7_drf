from django.urls import path

from main.apps import MainConfig
from main.views import HabitListAPIView, HabitCreateAPIView, MyHabitListAPIView, HabitDestroyAPIView, HabitUpdateAPIView

app_name = MainConfig.name

urlpatterns = [
    # Паттерны для Generic Habit - привычек
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),  # просмотр публичных привычек
    path('habit/my_habit/', MyHabitListAPIView.as_view(), name='my_habit_list'),  # просмотр только своих привычек
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),  # Создание привычки
    path('habit/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),

]
