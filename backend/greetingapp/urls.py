from django.urls import path
from greetingapp import views

urlpatterns = [
    path('greet', views.greet_view)
]