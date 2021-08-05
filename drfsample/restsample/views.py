from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics,status,viewsets #new
from django.contrib.auth.models import User #new
from django.contrib.auth import authenticate #new

from ajaxsample.models import Poll,Choice,Vote,GroupPoll

from .serializers import PollSerializers,ChoiceSerializer,VoteSerializer,GroupPollSerializers,UserSerializer #new


from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger('django')

# توضیحات
def samplepage(request):
    return render(request, 'useApi.html',{})

class simpleView(APIView):
    def get(self,request,*args, **kwargs):
        obj = {
            'maktab':'sharif',
            'simpleList':[1,2,3,4,5]
        }
        return Response({'message':'it is worked','obj':obj},status= status.HTTP_200_OK)

class pollView(APIView):
    
    def get(self,request,*args, **kwargs):
        # poll  = Poll.objects.get(id = 2)
        polls  = Poll.objects.all() 
        serializer = PollSerializers(polls, many = True)
        # https://stackoverflow.com/questions/61701946/original-exception-text-was-queryset-object-has-no-attribute-client
        # serializer = PollSerializers(polls,many=True)
        # serializer = PollSerializers(polls,many=True,context={'request': request}) #for HyperlinkedRelatedField add context
        return Response({'poll':serializer.data})


class PollDetail(APIView):
    def get(self, request, pk):
        # https://stackoverflow.com/questions/3090302/how-do-i-get-the-object-if-it-exists-or-none-if-it-does-not-exist-in-django
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializers(poll).data
        return Response(data)



# DRF generic views to simplify code
class PollListGenerics(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializers

class PollCreateGenerics(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializers

class PollDetailGenerics(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializers


# # step one
# class ChoiceList(generics.ListCreateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

# class CreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer

#end step one

#step two   
class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer


# url : http://localhost:8000/api/polls/1/choices/2/vote
# method : post 
# data : {"voted_by": 1}
class CreateVote(APIView):
    serializer_class = VoteSerializer
    def post(self, request, pk, choice_pk):
        # voted_by = request.data.get("voted_by")
        # data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        data = {'choice': choice_pk}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#end step two

class GroupPollList(generics.ListAPIView):
    queryset = GroupPoll.objects.all()
    serializer_class = GroupPollSerializers

class PollViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializers




#url : 127.0.0.1:8000/api/users
# method : post
#  data : {"username": "maktab","email": "maktab@gmail.com","password": "1qaz!QAZ123"}
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer



class LoginView(APIView):
    # permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)



