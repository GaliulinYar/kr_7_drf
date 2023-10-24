from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Добавляем админа"""
        user = User.objects.create(
            email='yaroslav66@list.ru',
            first_name='Admin',
            last_name='тут фамилия наверное',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('qwerty')
        user.save()
