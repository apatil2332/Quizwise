from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name="examiner_home"),
    path('questions/create', views.create_question, name="create_question"),
    path('questions', views.view_questions, name="view_questions"),
    path('questions/category/create', views.create_question_category, name="create_question_category"),
    path('questions/category/map', views.map_question_category, name="map_question_category"),
    path('questions/category/edit', views.edit_questions, name="edit_questions"),
    
]