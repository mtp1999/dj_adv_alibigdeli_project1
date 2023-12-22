from rest_framework.permissions import IsAuthenticated
from appTodo.models import Job
from .serializers import JobSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import JobListPagination
from .filters import JobListFilter


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = JobSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = JobListFilter
    search_fields = ["name"]
    ordering_fields = ["created_date"]
    pagination_class = JobListPagination

    def get_queryset(self):
        queryset = Job.objects.filter(user=self.request.user.profile)
        return queryset
