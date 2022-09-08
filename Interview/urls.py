from django.urls import path

from Interview.views import InterviewRegister

urlpatterns = [
    path('i/', InterviewRegister.as_view()),
]