from django.urls import path

from Interview.views import InterviewRegister, CommentListAPIView, CommentCreateAPIView, CommentDetailAPIView, CommentUpdateAPIView


urlpatterns = [
    path('i/', InterviewRegister.as_view()),
    path('c/', CommentCreateAPIView.as_view()),
    path('c2/', CommentListAPIView.as_view()),
    path('c3/<int:pk>', CommentDetailAPIView.as_view()),
    path('c4/<int:pk>', CommentUpdateAPIView.as_view())
]