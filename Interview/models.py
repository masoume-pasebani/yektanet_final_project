from django.db import models

# Create your models here.
from accounts.models import Interviewer, Applicant


class Interview(models.Model):
    TYPES = (
        ('Telephone interview', 'Telephone interview'),
        ('Technical interview', 'Technical interview'),
        ('Code interview', 'Code interview'),
        ('Final interview', 'Final interview'),
    )
    date = models.DateTimeField()
    interviewer = models.ForeignKey(Interviewer, null=True, on_delete=models.CASCADE)
    types = models.CharField(max_length=30, choices=TYPES)


class Comment(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class InterviewApplication(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)


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

