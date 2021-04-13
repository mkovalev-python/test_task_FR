"""
Author: mkovalev
Date: 13/04/2021 11:25

"""


from django.urls import path


from API_v0.user.views import ActivePoll, GetCheckPolls

urlpatterns = [
    path('poll/', ActivePoll.as_view()),
    path('poll/get/answers/', GetCheckPolls.as_view()),


]