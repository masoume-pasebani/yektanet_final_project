from django.urls import path
from .views import ApplicantRegisterView, InterviewerRegisterView, HRRegisterView, EditApplicantProfileView, EditInterviewer

urlpatterns = [
    path('applicant-register/', ApplicantRegisterView.as_view()),
    path('interviewer-register/', InterviewerRegisterView.as_view()),
    path('hr-register/', HRRegisterView.as_view()),
    path('edit-applicant/<int:pk>', EditApplicantProfileView.as_view()),
    path('edit-interviewer/<int:pk>', EditInterviewer.as_view())
]