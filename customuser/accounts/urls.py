from django.urls import path
from .views import SignUpView,simpleLogin,LoginRequiredTest,testLogin,updateTestView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('test/', LoginRequiredTest.as_view(), name='login-test'),
    path('simple-login/', simpleLogin, name='simple-login'),
    path('test2/', testLogin, name='testLogin'),
    path('simple-update/<int:pk>/<str:type>', updateTestView.as_view()),
]