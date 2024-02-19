from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from appTodo.models import Job
from .serializers import JobSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import JobListPagination
from .filters import JobListFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
from time import sleep


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = JobListFilter
    search_fields = ["name"]
    ordering_fields = ["created_date"]
    pagination_class = JobListPagination

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def get_weather(city_name):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    params = {'q': city_name, 'key': 'e4e2692b7e03481e86692308241602'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_info = {
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
            }
            return weather_info
        else:
            return response.status_code
    except requests.exceptions.RequestException as e:
        print('exception error')
        print(e)
        return None


class TehranWeatherAPIView(APIView):

    # caching for 20 minutes
    @method_decorator(cache_page(1200))
    def get(self, request, format=None):
        sleep(4)
        weather_info = get_weather('Tehran')
        return Response({'detail': weather_info})