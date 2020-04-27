from django.urls import path

from core import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]

