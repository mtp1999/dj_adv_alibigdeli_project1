from django.core.management.base import BaseCommand
import faker
from appBlog.models import Post, Category
from appAccount.models import Profile
import datetime


category_list = ["design", "develop", "security"]


class Command(BaseCommand):
    help = "create category and post using Faker module"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = faker.Faker()

    def handle(self, *args, **options):
        profile = Profile.objects.get(user__email="test.test@gmail.com")
        for _ in category_list:
            Category.objects.get_or_create(name=_)
        for _ in range(10):
            post = Post.objects.create(
                title=self.faker.sentence(nb_words=2),
                content=self.faker.paragraph(nb_sentences=4),
                author=profile,
                published_date=datetime.datetime.now(),
            )
            print(post.pk)
