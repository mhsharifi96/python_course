from django.urls import path
from .views import SignUpView,simpleLogin


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('simple-login/', simpleLogin, name='simple-login'),
]