from django.test import TestCase, Client
from django.urls import reverse
from appAccount.models import User
from appBlog.models import Post
from datetime import datetime


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("admin.admin@gmail.com", "a123456d")
        self.post = Post.objects.create(
            title="post title",
            content="post content",
            author=self.user.profile,
            published_date=datetime.now(),
        )

    def test_home_view_response_successfully(self):
        url = reverse("appBlog:home")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="appBlog/index.html")

    def test_single_view_logged_in_200(self):
        self.client.force_login(self.user)
        url = reverse("appBlog:single", kwargs={"pid": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_single_view_anonymous_200(self):
        url = reverse("appBlog:single", kwargs={"pid": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
