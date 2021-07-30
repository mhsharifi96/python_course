from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import simpleView,samplepage,pollView,PollDetail,PollListGenerics,\
    PollDetailGenerics,ChoiceList,CreateVote,PollViewSet,GroupPollList,\
        UserCreate,LoginView,PollCreateGenerics

router = DefaultRouter()
router.register('polls-set', PollViewSet, basename='polls_set')


urlpatterns = [
    path('',samplepage, name='index'),
    path('simple',simpleView.as_view(), name='simple'),
    path('polls/',pollView.as_view(), name='api-polls'),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path('g-polls/',PollListGenerics.as_view(), name='_polls'),
    path('g-polls/create/',PollCreateGenerics.as_view(), name='_polls'),
    path("g-polls/<int:pk>/", PollDetailGenerics.as_view(), name="_detail"),
    path("group/", GroupPollList.as_view(), name="group_list"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"), #step one
    # path("vote/", CreateVote.as_view(), name="create_vote"), #step one
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"), #step two
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name= "create_vote"), #step two
    path("users/", UserCreate.as_view(), name="user_create"), #register user
    path("login/", LoginView.as_view(), name="login"), #login user
    
]


urlpatterns += router.urls