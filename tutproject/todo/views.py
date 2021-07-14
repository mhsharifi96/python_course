from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from datetime import datetime

from .forms import SimpleForm



def CreateTodo(request):
   
    if request.method == "POST" :
        # print('this is post method')
        # print(dict(request.POST.items()))
        # print(request.POST['title'])
        # print(request.POST['description'])
        form = SimpleForm(request.POST)
        if form.is_valid() :
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            print('desc',description)
            print("form is valid nice work :)") 
            return HttpResponse('form is valid nice work :)')
        else :
            print (form.is_valid())
            print (type(form.errors))
            return JsonResponse(form.errors)
    
    else : 
         
        form = SimpleForm()
        # return HttpResponse('hello this is first page')
        return render(request,'todo.html',{"test":"this's worked !","form":form})


def CreateTodo1(request):
   
   
    form = SimpleForm(request.POST or None)
    if form.is_valid() :
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        print('desc',description)
        print("form is valid nice work :)") 
        return HttpResponse('form is valid nice work :)')
    

    
    # return HttpResponse('hello this is first page')
    return render(request,'todo.html',{"test":datetime.now()
                                    ,"form":form})




