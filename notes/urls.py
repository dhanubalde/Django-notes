from django.urls import path
from . import views
urlpatterns = [
    path('', views.TaskList, name="tasks"),
    path('<str:pk>/', views.TaskDetail, name="task"),
    path('<str:pk>/delete/', views.TaskDelete, name="delete"),
]