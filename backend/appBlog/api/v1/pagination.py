from rest_framework import pagination
from rest_framework.response import Response

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'appBlog.api.v1.pagination.PostListPagination',
    'PAGE_SIZE': 3
}


class PostListPagination(pagination.PageNumberPagination):
    page_size = 3

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })