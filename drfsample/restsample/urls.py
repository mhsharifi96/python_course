from django.urls import path
from .views import pollView,simpleView,samplepage

urlpatterns = [
    path('poll',pollView.as_view(), name='polls'),
    path('simple',simpleView.as_view(), name='simple'),
    path('',samplepage, name='index'),
    
]