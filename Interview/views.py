from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework import generics, status, authentication, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from Interview.models import Interview, Comment, Feedback
from Interview.serializers import InterviewRegisterSerializer, CommentSerializer, FeedbackSerializer
from accounts.models import Interviewer
from accounts.permissions import IsHR, IsOwnerOrReadOnly, IsInterviewer, IsHROrInterviewer, IsInterviewerOf


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
    permission_classes = [IsHR]



class CommentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class FeedbackCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsInterviewer]
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        interviewer = user.interviewer
        serializer.save(interviewer=interviewer)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(interviewer__user=self.request.user)
        return query_set

    def get_interview(self, pk):
        interviews = Interviewer.objects.get(user_id=pk).interview_set.all()
        return interviews


class EditInterview(generics.RetrieveUpdateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewRegisterSerializer
    permission_classes = [IsHR]