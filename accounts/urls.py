from django.urls import path
from .views import ApplicantRegisterView, InterviewerRegisterView, HRRegisterView

urlpatterns = [
    path('s/', ApplicantRegisterView.as_view()),
    path('s2/', InterviewerRegisterView.as_view()),
    path('s3/', HRRegisterView.as_view()),


]