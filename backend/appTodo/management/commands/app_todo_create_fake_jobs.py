from django.core.management.base import BaseCommand
import faker
from appTodo.models import Job
from appAccount.models import Profile
import random


class Command(BaseCommand):
    help = "create category and post using Faker module"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = faker.Faker()

    def handle(self, *args, **options):
        profile = Profile.objects.get(user__email="test.test@gmail.com")
        for _ in range(5):
            Job.objects.create(
                user=profile,
                name=self.faker.job(),
                status=random.choice(["done", "undone"]),
            )
