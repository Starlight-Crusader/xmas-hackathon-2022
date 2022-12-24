from django.urls import path
from greetingapp import views

urlpatterns = [
    path('greeting', views.greet_view)
]