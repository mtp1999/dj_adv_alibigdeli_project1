import django_filters
from appTodo.models import Job


class JobListFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'user': ['exact'],
            'status': ['exact'],
        }