from django.shortcuts import render,HttpResponse
from django.http import JsonResponse #new
from datetime import datetime
import json

from .models import Poll

from django.views.decorators.csrf import csrf_exempt


def ajaxDesc(request):


    return render(request,'index.html',{})


def ajaxSample(request):
    if request.method == 'POST'  and request.is_ajax():
        print(dict(request.POST.items()))
        # print(request.is_ajax())
        username = request.POST['username']
        message = "HI " + username + ' now Time : '+ str(datetime.now())
        polls = Poll.objects.all()
        if username : 
            print('test if')
            polls = polls.filter(question__contains = username)
        print()
        return JsonResponse({
            'message':message,
            'polls':list(polls.values())
        })

    return render(request,'sample.html',{})


@csrf_exempt
def apiSample(request):
    polls = Poll.objects.all()
    return JsonResponse({        
            'polls':list(polls.values())
        })