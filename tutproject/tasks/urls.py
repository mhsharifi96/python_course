from django.urls import path
from .views import *
urlpatterns = [
    path('delete/<int:id>/', delete, name='delete_task'),
    path('complete/<int:id>/', complete, name='completed_task'),
    path('list/', TasksView.as_view(), name='tasks_list'),
    path('page/', sample_paginator, name='sample_paginator'),
    path('', tasks, name='tasks'),
]
