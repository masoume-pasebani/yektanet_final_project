from django.urls import path
from .views import ApplicantRegisterView, InterviewerRegisterView, HRRegisterView, EditApplicantProfileView, EditInterviewer

urlpatterns = [
    path('s/', ApplicantRegisterView.as_view()),
    path('s2/', InterviewerRegisterView.as_view()),
    path('s3/', HRRegisterView.as_view()),
    path('e/<int:pk>', EditApplicantProfileView.as_view()),
    path('e2/<int:pk>', EditInterviewer.as_view())


]