from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from accounts.models import Applicant, Interviewer, HR


class ApplicantSignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})
    email = serializers.EmailField(max_length=100)

    def save(self, **kwargs):
        user_model: User = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        email = self.validated_data.pop('email')
        user = user_model.objects.create_user(username=username, password=password)

        Token.objects.create(user=user)

        applicant = super().save(user=user)
        user.groups.add(Group.objects.get(name='Applicant'))

        return applicant

    class Meta:
        model = Applicant
        fields = ('id', 'username', 'password','email', 'first_name', 'last_name', 'resume', 'linkedin', 'age', 'gender', 'status')

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
    email = serializers.EmailField(max_length=200)

    def save(self, **kwargs):

        user_model: User = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        email = self.validated_data.pop('email')
        user = user_model.objects.create_user(username=username, password=password, email=email)

        Token.objects.create(user=user)
        interviewer = super().save(user=user)
        user.groups.add(Group.objects.get(name='Interviewer'))

        return interviewer

    class Meta:
        model = Interviewer
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class HRSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True, style={'input_type': 'password', 'placeholder': 'Password'})
    email = serializers.EmailField(max_length=200)

    def save(self, **kwargs):

        user_model: User = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        email = self.validated_data.pop('email')
        user = user_model.objects.create_user(username=username, password=password, email= email)
        user.is_staff = True
        user.is_superuser = True
        Token.objects.create(user=user)
        user.save()
        hr = super().save(user=user)
        user.groups.add(Group.objects.get(name='HR'))

        return hr

    class Meta:
        model = HR
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'phone_number')
