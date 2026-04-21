from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.body[:50]
