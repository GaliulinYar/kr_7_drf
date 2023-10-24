from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """ Пагинация вывода по 5 записей максимум 50"""

    page_size = 5
    page_size_query_param = 'per_page'
    max_page_size = 50
