"""
Author: mkovalev
Date: 13/04/2021 8:43

"""

from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('login/refresh/', refresh_jwt_token),
]
