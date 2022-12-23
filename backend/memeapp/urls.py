from django.urls import path
from memeapp import views

urlpatterns = [
    path('getmeme', views.GetMeme.as_view()),
]
