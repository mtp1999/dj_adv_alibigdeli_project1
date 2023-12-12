import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import datetime
from appAccount.models import User
from appBlog.models import Category


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user('admin.admin@gmail.com', 'a123456d')
    return user


@pytest.fixture
def category():
    obj = Category.objects.create(name="any name")
    return obj


@pytest.mark.django_db
class TestPost:
    posts_list_url = reverse("appBlog:api-v1:posts-list")

    def test_post_list_200(self, api_client):
        response = api_client.get(self.posts_list_url)
        assert response.status_code == 200

    def test_post_create_status_401(self, api_client):
        data = {
            'title': "post title",
            'content': "post content",
            'author': 1,
            'published_date': datetime.now(),
        }
        response = api_client.post(self.posts_list_url, data)
        assert response.status_code == 401

    def test_post_create_status_201(self, api_client, common_user, category):
        api_client.force_login(user=common_user)
        data = {
            'title': "post title",
            'content': "post content",
            'author': common_user.profile,
            'published_date': datetime.now(),
            'categories': [category.pk],
        }
        response = api_client.post(self.posts_list_url, data)
        assert response.status_code == 201

    def test_post_create_invalid_data_status_400(self, api_client, common_user, category):
        api_client.force_login(user=common_user)
        data = {
            'title': "",    # blank title not allowed
            'content': "post content",
            'author': common_user.profile,
            'published_date': datetime.now(),
            'categories': [2],  # not exist category with this pk id
        }
        response = api_client.post(self.posts_list_url, data)
        assert response.status_code == 400
