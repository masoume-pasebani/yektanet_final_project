from typing import Union

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from accounts.models import Interviewer, Applicant, HR


class Interview(models.Model):
    TYPES = (
        ('Telephone Interview', 'Telephone Interview'),
        ('Technical Interview', 'Technical Interview'),
        ('Code Interview', 'Code Interview'),
        ('Final Interview', 'Final Interview'),
    )
    date = models.DateTimeField()
    interviewer = models.ForeignKey(Interviewer, null=True, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, null=True, on_delete=models.CASCADE)
    types = models.CharField(max_length=30, choices=TYPES, default='Telephone Interview')

    def __str__(self):
        return self.interviewer+ ' with '+ self.applicant


class Comment(models.Model):
    #owner = models.ForeignKey(Interviewer, null=True, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

class Feedback(models.Model):
    RATE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    feedback = models.TextField(max_length=300)
    rate = models.CharField(max_length=1, choices=RATE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

