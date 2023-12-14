from django.test import TestCase
from django.urls import reverse, resolve
from appBlog import views


class TestUrl(TestCase):
    def test_home_view(self):
        url = reverse("appBlog:home")
        self.assertEquals(resolve(url).func.view_class, views.HomeView)

    def test_blog_view(self):
        url = reverse("appBlog:blog")
        self.assertEquals(resolve(url).func.view_class, views.BlogView)

    def test_single_view(self):
        url = reverse("appBlog:single", kwargs={"pid": 1})
        self.assertEquals(resolve(url).func.view_class, views.SingleView)
