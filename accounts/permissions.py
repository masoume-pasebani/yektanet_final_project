from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import permissions


class IsApplicant(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Applicant').exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Applicant').exists():
            return True
        else:
            return False


class IsInterviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Interviewer').exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Interviewer').exists():
            return True
        else:
            return False


class IsHR(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='HR').exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='HR').exists():
            return True
        else:
            return False


class IsHROrInterviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Interviewer').exists() |\
                request.user.groups.filter(name='HR').exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Interviewer').exists() | \
                request.user.groups.filter(name='HR').exists():
            return True
        else:
            return False


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user




