from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework import generics, status


from Interview.models import Interview, Comment, Feedback
from Interview.serializers import InterviewRegisterSerializer, CommentSerializer, FeedbackSerializer
from accounts.permissions import IsInterviewer, IsHR, IsHROrInterviewer, IsOwnerOrReadOnly


class InterviewRegister(generics.CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewRegisterSerializer
    permission_classes = [IsHR]


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsHROrInterviewer]


class CommentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class FeedbackCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsInterviewer]


class EditInterview(generics.RetrieveUpdateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewRegisterSerializer
    permission_classes = [IsHR]