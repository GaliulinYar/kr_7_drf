from datetime import datetime
import pytz
from celery import shared_task
from main.models import Habit
from main.post_habit import handle
import requests


@shared_task
def time_for_every_day():

    timezone = pytz.timezone('Asia/Yekaterinburg')
    current_time_yek = datetime.now(timezone)
    current_time = current_time_yek.strftime('%H:%M')
    print(current_time)
    habits = Habit.objects.all()  # Получяем объекты Habit по фильтру раз в день

    for habit in habits:

        if habit.EVERY_DAY:  # каждые 24 часа
            if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                handle(habit.get_habit)  # Выполняем отправку

        if habit.ONCE_A_WEEK:
            if (current_time_yek - habit.create_time).days > 2:  # каждые 48 часов раз в два дня
                if current_time == habit.time_habit.strftime('%H:%M'):  #
                    handle(habit.get_habit)

        if habit.TWO_TIMES_A_WEEK:
            if (current_time_yek - habit.create_time).days > 3:  # каждые 72 часа раз в 3 дня
                if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                    handle(habit.get_habit)

        if habit.THREE_TIMES_A_WEEK:
            if (current_time_yek - habit.create_time).days > 4:  # каждые 96 часа раз в 4 дня
                if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                    handle(habit.get_habit)

        if habit.FOUR_TIMES_A_WEEK:
            if (current_time_yek - habit.create_time).days > 5:  # каждые 120 часа раз в 5 дней
                if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                    handle(habit.get_habit)

        if habit.FIVE_TIMES_A_WEEK:
            if (current_time_yek - habit.create_time).days > 6:  # каждые 144 часа или каждые 6 дней
                if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                    handle(habit.get_habit)

        if habit.SIX_TIMES_A_WEEK:
            if (current_time_yek - habit.create_time).days > 7:  # каждые 172 часа или каждые 7 дней
                if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                    handle(habit.get_habit)
