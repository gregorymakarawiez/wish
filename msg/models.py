from django.db import models
from django.utils import timezone


class Message(models.Model):

    message= models.TextField()
    creation_date = models.DateTimeField(blank=True, null=True)

    def create(self, message):
        self.message=message
        self.creation_date = timezone.now()
        self.save()