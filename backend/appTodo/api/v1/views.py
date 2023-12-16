from rest_framework.permissions import IsAuthenticatedOrReadOnly
from appTodo.models import Job
from .serializers import JobSerializer
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import JobListPagination
from .filters import JobListFilter


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
