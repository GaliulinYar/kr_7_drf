from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Habit
from user.models import User
# Create your tests here.


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.user.set_password('qwerty')
        self.user.save()

        self.moderator = User.objects.create(email='moderator@moderator.com', is_staff=True)
        self.moderator.set_password('1234')
        self.moderator.save()

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            place_habit="Походы в парк",
            time_habit="15:00",
            get_habit="Гуляем на свежем воздухе",
            nice_habit=True,
            associated_habit="Подарок себе вкусный мороженое",
            period_habit="Три раза в неделю",
            reward_habit="Положительные эмоции и активный отдых",
            time_limit=60,
            is_public=False
        )
        self.habit.save()

    def test_habit_create(self):
        """Тест пост запрос создание привычки"""
        url = 'http://127.0.0.1:8000/habit/create/'
        data = {
            "owner": self.user.pk,
            "place_habit": "Сбор продуктов",
            "time_habit": "10:00",
            "get_habit": "Планируем меню и готовим здоровую пищу",
            "nice_habit": False,
            "associated_habit": "Поддержка семьи и обмен рецептами",
            "period_habit": "Каждый день",
            "reward_habit": "Полезное питание и забота о близких",
            "time_limit": 120,
            "is_public": True
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

        data_error = data
        data_error['time_limit'] = 122
        response = self.client.post(url, data_error, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_habits(self):
        """Просмотр соих привычек"""
        url = 'http://127.0.0.1:8000/habit/my_habit/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_authenticate(user=self.moderator)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_list_habits_public(self):
        """тест на просмотр публичных привычекк"""
        url = 'http://127.0.0.1:8000/habit/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_update_habit(self):
        """Обновлениe привычки"""
        url = reverse('main:habit_update', kwargs={'pk': self.habit.id})
        data = {"get_habit": "изменил",
                "owner": self.user.pk,
                "id": self.habit.id
                }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['get_habit'], 'изменил')

    def test_delete_habit(self):
        """Тест на удаление привычки"""
        url = reverse('main:habit_delete', kwargs={'pk': self.habit.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
