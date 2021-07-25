from django.urls import path

from .views import ajaxSample,ajaxDesc,apiSample

urlpatterns = [
    path('',ajaxDesc, name='ajax-desc'),
    path('sample',ajaxSample, name='ajax-sample'),
    path('api',apiSample, name='api-sample'),
]
