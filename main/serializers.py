from rest_framework import serializers

from main.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра всех привычек всех пользователей"""
    class Meta:
        model = Habit
        fields = '__all__'
