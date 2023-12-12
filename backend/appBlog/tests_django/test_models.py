from django.test import TestCase
from appBlog.models import Post
from datetime import datetime
from appAccount.models import User


class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('admin.admin@gmail.com', 'a123456d')

    def test_post_create_with_valid_data(self):

        post = Post.objects.create(
            title="post title",
            content="post content",
            author=self.user.profile,
            published_date=datetime.now(),
        )
        self.assertEquals(post.title, "post title")