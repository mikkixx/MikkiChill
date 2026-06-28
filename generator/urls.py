from django.urls import path
from . import views

urlpatterns = [path('ideas/', views.idea_list, name='idea_list')]
