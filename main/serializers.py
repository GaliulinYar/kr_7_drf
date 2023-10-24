from rest_framework import serializers

from main.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра привычек"""

    class Meta:
        model = Habit
        fields = ['get_habit', 'owner', 'id']
