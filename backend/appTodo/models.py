from django.db import models
from appAccount.models import Profile


class Job(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    STATUS_CHOICES = (
        ('done', 'done'),
        ('undone', 'undone'),
    )
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='undone')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " ::: " + str(self.user) + " ::: " + str(self.name)
