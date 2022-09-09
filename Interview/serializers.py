from rest_framework import serializers

from Interview.models import Interview, Comment


class InterviewRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ('date', 'interviewer', 'applicant', 'types',)


class InterviewSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    interviewer = serializers.ReadOnlyField(source='interviewer.last_name')

    class Meta:
        model = Interview
        fields = ('id', 'interviewer', 'applicant', 'date', 'types')


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'interview', 'description', 'created_at', 'owner')
        read_only_fields = ('owner',)





