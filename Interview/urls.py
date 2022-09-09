from django.urls import path

from Interview.views import InterviewRegister, CommentListAPIView, CommentCreateAPIView , \
    CommentUpdateAPIView, FeedbackCreateAPIView, EditInterview

urlpatterns = [
    path('i/', InterviewRegister.as_view()),
    path('c/', CommentCreateAPIView.as_view()),
    path('c2/', CommentListAPIView.as_view()),
    path('c4/<int:pk>', CommentUpdateAPIView.as_view()),
    path('f/', FeedbackCreateAPIView.as_view()),
    path('i2/<int:pk>', EditInterview.as_view())
]