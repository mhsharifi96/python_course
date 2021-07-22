from django.urls import path
from .views import *
from django.views.generic import TemplateView,DetailView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
