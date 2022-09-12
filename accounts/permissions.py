from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import permissions

from Interview.models import Interview, Comment, Feedback
from accounts.models import Interviewer


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
        if request.user.groups.filter(name='HR').exists() |\
            request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='HR').exists()|\
                request.user.is_superuser:
            return True
        else:
            return False


class IsHROrInterviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Interviewer').exists() |\
                request.user.groups.filter(name='HR').exists() |\
                request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Interviewer').exists() |\
                request.user.groups.filter(name='HR').exists()|\
                request.user.is_superuser:
            return True
        else:
            return False


class IsNotInterviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Applicant').exists() |\
                request.user.groups.filter(name='HR').exists() | request.user.is_anonymous | request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Applicant').exists() | \
                request.user.groups.filter(name='HR').exists() | request.user.is_anonymous | request.user.is_superuser:
            return True
        else:
            return False


class IsNotInterviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Applicant').exists() |\
                request.user.groups.filter(name='HR').exists() | request.user.is_anonymous | request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Applicant').exists() | \
                request.user.groups.filter(name='HR').exists() | request.user.is_anonymous | request.user.is_superuser:
            return True
        else:
            return False


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Interviewer').exists() and request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsAdminOrOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:  # agar method haye get bashe va taghiri dar
            # database ijad nakonand mese method update ,unvaght ejaze dastresi dare
            return True

        if request.user.groups.filter(name='HR').exists() | request.user.is_superuser:  # if uswer loged in and is admin can access to all method
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class IsNotApplicant(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Interviewer').exists() |\
                request.user.groups.filter(name='HR').exists() | request.user.is_anonymous | request.user.is_superuser:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Interviewer').exists() | \
                request.user.groups.filter(name='HR').exists() | request.user.is_anonymous | request.user.is_superuser:
            return True
        else:
            return False

