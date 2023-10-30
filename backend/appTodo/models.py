from django.db import models
from appAccount.models import Profile
from django.shortcuts import reverse

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

    def return_email(self):
        return self.user.user.email

    def get_absolute_api_url(self):
        return reverse('appTodo:api-v1:jobs-detail', kwargs={'pk': self.pk})
