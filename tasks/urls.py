from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', view=views.TaskView.as_view() ),
    path('<int:id>', view=views.TaskDetailsView.as_view() )
]



