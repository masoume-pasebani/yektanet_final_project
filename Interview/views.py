from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.exceptions import ValidationError

from Interview.models import Interview
from Interview.serializers import InterviewRegisterSerializer
from accounts.permissions import IsInterviewer, IsHR


class InterviewRegister(generics.CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewRegisterSerializer
    permission_classes = [IsHR]


