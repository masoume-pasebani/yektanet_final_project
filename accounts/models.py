from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

TYPE = (
    (1, 'HR'),
    (2, 'interviewer'),
    (3, 'applicant')
)


class Applicant(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Being interviewed', 'Being interviewed'),
        ('Failed', 'Failed')
    )

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    resume = models.FileField(upload_to='resume/')
    linkedin = models.URLField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER, default='Male')
    status = models.CharField(max_length=25, choices=STATUS, default='Pending')

    def __str__(self):
        return self.first_name+' '+self.last_name


class Interviewer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name+' '+self.last_name


class HR(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name+' '+self.last_name