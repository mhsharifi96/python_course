from django.urls import path

from .views import ajaxSample,ajaxDesc,apiSample,jsonView,workWithApi

urlpatterns = [
    path('',ajaxDesc, name='ajax-desc'),
    path('json',jsonView, name='json-sample'),
    path('sample',ajaxSample, name='ajax-sample'),
    path('work-api',workWithApi, name='work-api'),
    path('api',apiSample, name='api-sample'),
]
