from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('create/', CreateTodo,name='createtodo'),
    path('create1/', CreateTodo1,name='createtodo1'),
]
