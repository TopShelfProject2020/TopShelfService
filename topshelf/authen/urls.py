from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from authen import views
from authen.views import Register

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.Register.as_view()),
]

# router = DefaultRouter()
# router.register(r'register', views.Register, basename='register')
#
#
# urlpatterns += router.urls
