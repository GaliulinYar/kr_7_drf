from django.core.validators import MaxValueValidator
from django.db import models
from django.conf import settings

NULLABLE = {
    'null': True,
    'blank': True
}


class Habit(models.Model):

    EVERY_DAY = 'Каждый день'
    ONCE_A_WEEK = 'Раз в два дня'
    TWO_TIMES_A_WEEK = 'Раз в три дня'
    THREE_TIMES_A_WEEK = 'Раз в четыре дня'
    FOUR_TIMES_A_WEEK = 'Раз в пять дня'
    FIVE_TIMES_A_WEEK = 'Раз в шесть дня'
    SIX_TIMES_A_WEEK = 'Раз в семь дня'

    PERIOD = (
        (EVERY_DAY, 'Каждый день'),
        (ONCE_A_WEEK, 'Раз в два дня'),
        (TWO_TIMES_A_WEEK, 'Раз в три дня'),
        (THREE_TIMES_A_WEEK, 'Раз в четыре дня'),
        (FOUR_TIMES_A_WEEK, 'Раз в пять дня'),
        (FIVE_TIMES_A_WEEK, 'Раз в шесть дня'),
        (SIX_TIMES_A_WEEK, 'Раз в семь дня'),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки',
                              **NULLABLE)  # создатель привычки, авторизованные пользователь
    place_habit = models.CharField(max_length=80, verbose_name='Место выполнения привычки')  # место выполнения привычки
    time_habit = models.TimeField(verbose_name='Время привычки')  # Время привычки
    get_habit = models.CharField(max_length=200, verbose_name='Что делаем(например, приседаем)')  # указание привычки - действие
    nice_habit = models.BooleanField(verbose_name='Приятная привычка')  # Признак приятной привычки Тру или Фолс
    associated_habit = models.CharField(max_length=100, verbose_name='Приятная связанная привычка ')  # Связанная привычка

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания привычки')
    period_habit = models.CharField(choices=PERIOD, verbose_name='Периодичность') # Периодичность привычки
    reward_habit = models.CharField(max_length=50, verbose_name='Награда за выполнение привычки')  # Награда за выполнение привычки
    time_limit = models.PositiveSmallIntegerField(
        verbose_name='Время на выполнение привычки (в секундах)',
        validators=[MaxValueValidator(120)]
    )  # Время на выполнение привычки (в секундах) не более 120 сек

    is_public = models.BooleanField(verbose_name='Публичность') # Признак публичности (True - видно, False - не видно)

    def __str__(self):
        return f'Я буду {self.get_habit} в {self.time_habit} в {self.place_habit} и получу за это{self.reward_habit}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
