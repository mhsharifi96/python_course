from django.shortcuts import render,HttpResponse
from django.http import JsonResponse #new
from datetime import datetime
import json

from .models import Poll

from django.views.decorators.csrf import csrf_exempt
from pprint import pprint

def ajaxDesc(request):
    return render(request,'index.html',{})



# def ajaxSample(request):
#     if request.method == 'POST':
#         pprint(dict(request.POST.items()))
#         print(request.POST['inputText1'])
#         print(request.POST['sampleObj'])
#         print(type(request.POST['sampleObj']))


#     return render(request,'sample.html',{})

def ajaxSample(request):
    if request.method == 'POST'  and request.is_ajax():
        print(dict(request.POST.items())) # محتویات درخواست مشاهده کنید
        # print(request.is_ajax())  #print True
        inputText = request.POST['inputText']
        
        polls = Poll.objects.all() #new
        if inputText : 
            # print('test if')
            polls = polls.filter(question__contains = inputText)


        message = "HI " + inputText + ' now Time : '+ str(datetime.now())
        return JsonResponse({
            'message':message,
            # 'polls':polls   #error
            'polls':list(polls.values())
        })

    return render(request,'sample.html',{})

def jsonView(request):
    # نمونه تستی json 
    return JsonResponse({
        'message' : "this is for test :)"+str(datetime.now()),
        'test3' : "test3",
        'testList' : [1,2,3,4],
        'testobj' : {'numbers':[1,2,3,4,5,6],'maktab':'sharif'}
    })



@csrf_exempt
def apiSample(request):
    polls = Poll.objects.all()
    return JsonResponse({        
            'polls':list(polls.values())
        })



def workWithApi(request):
    return render(request,'work_api.html',{})