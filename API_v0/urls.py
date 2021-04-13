"""
Author: mkovalev
Date: 13/04/2021 8:43

"""

from django.urls import path, include
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('login/refresh/', refresh_jwt_token),

    path('admin/', include('API_v0.admin.urls')),
    path('user/', include('API_v0.user.urls')),

    path('swagger/', get_schema_view(title='Rest API Document',
                                     permission_classes=(permissions.AllowAny,),
                                     public=True,
                                     )),

]
