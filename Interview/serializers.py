from rest_framework import serializers

from Interview.models import Interview


class InterviewRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ('date', 'interviewer', 'types',)


class InterviewSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    interviewer = serializers.ReadOnlyField(source='interviewer.last_name')

    class Meta:
        model = Interview
        fields = ('id', 'interviewer', 'date', 'types')

