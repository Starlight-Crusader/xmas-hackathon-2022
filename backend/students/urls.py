from django.urls import path
from students import views


urlpatterns = [
    path('create', views.create_student),
    path('delete', views.delete_student),
    path('list', views.list_students)
]
