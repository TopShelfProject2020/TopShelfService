from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from authen.views import Register

urlpatterns = [
    path('login/', obtain_jwt_token),

    path('register/', Register.as_view())
]