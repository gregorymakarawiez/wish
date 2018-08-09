from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from account.models import Employee, Unit
#from viewflow.models import Process
import datetime




#class Task(Process):
class Task(models.Model):

    state_choices=(
        (1, 'WAITING_FOR_VALIDATION'),
        (2, 'WAITING_FOR_IMPLEMENTATION'),
        (3, 'WAITING_FOR_APPROVAL'),
        (4, 'COMPLETED'),
        (5, 'REFUSED'),

    )
    state= models.CharField(choices=state_choices, default=0, max_length=1)

    # creation step
    creator = models.ForeignKey(Employee, related_name='task_creator', on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    headline = models.CharField(max_length=200)
    problem = models.TextField()
    proposal = models.TextField()
    validator = models.ForeignKey(Employee, related_name='task_validator', on_delete=models.SET_NULL, null=True)

    # validation step
    validation_date = models.DateTimeField(blank=True, null=True)
    validation_choice= models.CharField(choices=state_choices, default=5, max_length=1)
    validation_text = models.TextField()
    task_due_date = models.DateField(blank=True, default=datetime.date.today(), null=True)
    standard_update_due_date = models.DateField(blank=True, default=datetime.date.today(), null=True)
    implementer = models.ForeignKey(Employee, related_name='task_implementer', on_delete=models.SET_NULL, null=True)
    mailing_list = models.ForeignKey(Unit, related_name='task_mailing_list', on_delete=models.SET_NULL, null=True)

    # implementation step
    implementation_date = models.DateTimeField(blank=True, null=True)
    approver = models.ForeignKey(Employee, related_name='task_approver', on_delete=models.SET_NULL, null=True)

    # final approval and submission
    completion_date = models.DateTimeField(blank=True, null=True)
    approved= models.BooleanField(default=False)

    def create(self,actor):
        self.state=1
        self.creator=actor
        self.creation_date = timezone.now()
        self.save()

    def validate(self,actor):
        self.state=self.validation_choice
        self.validation_date = timezone.now()
        self.save()

    def submit(self, actor):
        self.implementation_date = timezone.now()
        self.state=3
        self.save()

    def approve(self, actor):
        if self.approved:
            self.state=4
        else:
            self.state=3

        self.completion_date = timezone.now()
        self.save()

    def __str__(self):
        return self.headline



