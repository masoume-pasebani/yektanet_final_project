from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from accounts.models import Applicant, Interviewer, HR


class ApplicantSignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})

    def save(self, **kwargs):
        user_model: User = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        user = user_model.objects.create_user(username=username, password=password)

        Token.objects.create(user=user)

        applicant = super().save(user=user)
        user.groups.add(Group.objects.get(name='Applicant'))

        return applicant

    class Meta:
        model = Applicant
        fields = ('username', 'password', 'first_name', 'last_name', 'resume', 'linkedin', 'age', 'gender')

    def to_representation(self, instance):
        return ApplicantSerializer(instance).data


class ApplicantSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Applicant
        fields = ['id', 'first_name', 'last_name', 'resume', 'linkedin', 'age', 'gender', 'status']


class InterviewerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})

    def save(self, **kwargs):

        user_model: User = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        user = user_model.objects.create_user(username=username, password=password)

        Token.objects.create(user=user)
        interviewer = super().save(user=user)
        user.groups.add(Group.objects.get(name='Interviewer'))

        return interviewer

    class Meta:
        model = Interviewer
        fields = ('username', 'password', 'first_name', 


class HRSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})

    def save(self, **kwargs):

        user_model: User = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        user = user_model.objects.create_user(username=username, password=password)

        Token.objects.create(user=user)
        user.is_superuser = True
        user.is_staff = False
        hr = super().save(user=user)
        user.groups.add(Group.objects.get(name='HR'))

        return hr

    class Meta:
        model = HR
        fields = ('username', 'password', 'first_name', 'last_name', 'phone_number')
