from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from accounts.models import Applicant, Interviewer, HR
from accounts.permissions import IsOwnerOrReadOnly, IsHR, IsInterviewer, IsNotInterviewer, IsAdminOrOwner
from accounts.serializers import ApplicantSignUpSerializer, InterviewerSerializer, ApplicantSerializer, HRSerializer


class ApplicantRegisterView(generics.CreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSignUpSerializer
    permission_classes = [IsNotInterviewer]


class InterviewerRegisterView(generics.CreateAPIView):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer
    permissions_classes = []


class HRRegisterView(generics.CreateAPIView):
    queryset = HR.objects.all()
    serializer_class = HRSerializer
    permission_classes = [IsAdminUser]


class EditApplicantProfileView(generics.RetrieveUpdateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSignUpSerializer
    permission_classes = [IsAdminOrOwner]


class EditInterviewer(generics.RetrieveUpdateAPIView):
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer
    permission_classes = [IsOwnerOrReadOnly]


