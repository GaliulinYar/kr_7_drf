from django.urls import path

from main.apps import MainConfig
from main.views import HabitListAPIView, HabitCreateAPIView, MyHabitListAPIView

app_name = MainConfig.name

urlpatterns = [
    # Паттерны для Generic Habit - привычек
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/my_habit/', MyHabitListAPIView.as_view(), name='my_habit_list'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='lesson_create'),
    # path('lesson/<int:pk>/detail/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    # path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    # path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

]