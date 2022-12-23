from django.apps import AppConfig


<<<<<<<< HEAD:backend/quizzes/apps.py
class QuizzesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quizzes'
========
class ParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parser'
>>>>>>>> 2415ddbac93b1075a59ff5f52feed3ffb58e2717:backend/parse/apps.py
