from django.urls import path
from quizzes import views


urlpatterns = [
    path('manage', views.QuestionsList.as_view()),
    path('create', views.GetQuestions.as_view())
]
