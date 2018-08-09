from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User





class Unit(models.Model):

    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return '%s' % (self.name)



class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    manager = models.ForeignKey('self',on_delete=models.SET_NULL, blank=True, null=True)
    is_manager = models.BooleanField(default=False, blank=True)
    is_continuous_improvement_officer= models.BooleanField(default=False, blank=True)
    subscribed_to_newsletter = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


    # overriden to delete OneToOneField user
    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


