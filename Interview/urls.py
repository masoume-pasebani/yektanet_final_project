from django.urls import path

from Interview.views import InterviewRegister, CommentCreateAPIView, \
    CommentUpdateAPIView, FeedbackCreateAPIView, EditInterview, CommentListAPIView

urlpatterns = [
    path('create-interview/', InterviewRegister.as_view()),
    path('create-comment/', CommentCreateAPIView.as_view()),
    path('comment-list/', CommentListAPIView.as_view()),
   # path('edit-comment/<int:pk>', CommentUpdateAPIView.as_view()),
    path('feedback/', FeedbackCreateAPIView.as_view()),
    path('edit-interview/<int:pk>', EditInterview.as_view())
]