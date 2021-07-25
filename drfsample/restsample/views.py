from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ajaxsample.models import Poll,Choice,Vote

from .serializers import PollSerializers
# Create your views here.







class simpleView(APIView):
    
    def get(self,request,*args, **kwargs):

        return Response({'message':'it is worked'})


class pollView(APIView):
    
    def get(self,request,*args, **kwargs):
        poll  = Poll.objects.get(id = 1)
        serializer = PollSerializers(poll)
        
        return Response({'poll':serializer.data})





def samplepage(request):

    return render(request, 'useApi.html',{})