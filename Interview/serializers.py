from rest_framework import serializers

from Interview.models import Interview, Comment, Feedback


class InterviewRegisterSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Interview
        fields = ('id', 'date', 'interviewer', 'applicant', 'types',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'interview', 'description', 'created_at', 'owner')
       # read_only_fields = ('owner',)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'interviewer', 'interview', 'feedback', 'rate', 'created_at')

