from django.urls import path
from .views import *
from django.views.generic import TemplateView,DetailView
urlpatterns = [
    path('delete/<int:id>/', delete, name='delete_task'),
    path('complete/<int:id>/', complete, name='completed_task'),
    path('list/', TasksView.as_view(), name='tasks_list'),
    path('page/', sample_paginator, name='sample_paginator'),
    path('dynamic/', dynamic, name='dynamic_list'),
    path('maktab/', maktabsample, name='maktab_sample'),
    path('simple/', simple, name='simple_form'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about_page'),
    path('about-view/', aboutView.as_view(), name='about_page1'),
    path('task-view/', tasksListViews.as_view(), name='task'),
    path('task-detail/<int:pk>/', tasksDetailViews.as_view(), name='task-detail'),
    path('', tasks, name='tasks'),

]
