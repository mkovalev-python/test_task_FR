"""
Author: mkovalev
Date: 13/04/2021 11:25

"""


from django.urls import path

from API_v0.admin.views import PollApi, QuestionApi

urlpatterns = [
    path('poll/post/', PollApi.as_view()),
    path('poll/put/<int:pk>/', PollApi.as_view()),
    path('poll/del/<int:pk>/', PollApi.as_view()),
    path('question/post/', QuestionApi.as_view()),
    path('question/put/<int:pk>/', QuestionApi.as_view()),
    path('question/del/<int:pk>/', QuestionApi.as_view()),

]