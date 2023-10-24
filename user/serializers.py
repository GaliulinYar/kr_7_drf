from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для юзера"""

    class Meta:
        # показываем все поля Юзера
        model = User
        fields = ['email', 'first_name', 'id']
