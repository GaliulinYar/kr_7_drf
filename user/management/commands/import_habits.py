import os
import django
import json

from django.core.management import BaseCommand

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from main.models import Habit


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Открываем файл JSON и загружаем его содержимое
        with open('user/management/commands/habit_list.json', 'r') as json_file:
            habit_data = json.load(json_file)

        # Создаем экземпляры модели Habit на основе данных из JSON
        for habit_entry in habit_data:
            habit = Habit(
                owner_id=habit_entry['fields']['owner'],
                place_habit=habit_entry['fields']['place_habit'],
                time_habit=habit_entry['fields']['time_habit'],
                get_habit=habit_entry['fields']['get_habit'],
                nice_habit=habit_entry['fields']['nice_habit'],
                associated_habit=habit_entry['fields']['associated_habit'],
                period_habit=habit_entry['fields']['period_habit'],
                reward_habit=habit_entry['fields']['reward_habit'],
                time_limit=habit_entry['fields']['time_limit'],
                is_public=habit_entry['fields']['is_public']
            )
            habit.save()
