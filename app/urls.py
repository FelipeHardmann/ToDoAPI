from app.views import ToDoListAndCreate, ToDoDetailChangeAndView
from django.urls import path

urlpatterns = [
    path('', ToDoListAndCreate.as_view()),
    path('<int:pk>/', ToDoDetailChangeAndView.as_view())
]
