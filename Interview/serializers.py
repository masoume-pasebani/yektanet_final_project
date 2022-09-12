from rest_framework import serializers, request

from Interview.models import Interview, Comment, Feedback
from accounts.models import Interviewer
from accounts.serializers import InterviewerSerializer


class InterviewRegisterSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:

        model = Interview
        fields = ('id', 'date', 'interviewer', 'applicant', 'types',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'interview', 'description', 'created_at')





class FeedbackSerializer(serializers.ModelSerializer):
    interviewer = InterviewerSerializer(read_only=True)
    class Meta:
        model = Feedback
        fields = ('id',  'feedback','interviewer', 'interview', 'rate', 'created_at')


