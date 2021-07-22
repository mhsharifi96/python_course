from django.shortcuts import  render, redirect, reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views import  View
from django.views.generic import ListView,TemplateView,DetailView
from django.core.paginator import Paginator
from pprint import pprint


from .models import  Task
from .forms import TaskForm,TaskManualForm,ExampleForm,simpleForm
from django.template import RequestContext
import json
# Create your views here.

def tasks(request):
    if request.method == 'POST':
        # this is wehere POST request is accessed
        form = TaskForm(request.POST or None)
        if form.is_valid():
            
            temp = form.save(commit=False)
            
            temp.save()
            form = TaskForm()
        tasks = Task.objects.all().order_by('priority')
        return render(request, 'tasks.html', {'form': form, 'tasks': tasks})
    else:
        
        form = TaskForm()
        tasks = Task.objects.all().order_by('priority')
        
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks})


def delete(request, id):
    if Task.objects.filter(id=id).delete():
        
        return redirect(reverse('tasks'))
    else:
        return HttpResponse("You are not allowed to access this resource")

def complete(request, id):
    
    try:
        task=Task.objects.get(id=id)
        if task.complete:
            task.complete = 0
        else:
            task.complete = 1
        task.save()
        return redirect(reverse('tasks'))
    except Exception:
        return HttpResponse("Sorry You are not allowed to access This task ")
    
    return HttpResponse("You are not allowed to access this resource")


# """
# برای اجرای این قسمت هر استپ را ازکامنت بیرون آورید و سایر استپ ها رو کامنت کنید 
# """

# START OF STEP


# without form
# start step 1
# class TasksView(View):
#     def get(self,request,*args, **kwargs):
#         print('this get page')
#         tasks = Task.objects.all()
#         return render(request,'lists.html',{'tasks': tasks})

#     def post(self,request,*args, **kwargs):
#         print(dict(request.POST.items()))
#         if request.POST['title'] and  request.POST['description']:
#             print('its ok')
#             created = Task.objects.create(title= request.POST['title'],description = request.POST['description'],priority=request.POST['priority'])
#             if created :
#                 print('object create successfully')
#                 return redirect(reverse('tasks_list'))

#         return HttpResponse("this is post method on taskView")
 # end step 1 


# # use forms.Form
# #step 2
class TasksView(View):

    def get(self,request,*args, **kwargs):
        form = TaskManualForm()
        # form = ExampleForm()
        print('this get page')
        tasks = Task.objects.all()
        return render(request,'lists_step2.html',{'tasks': tasks,'form':form})

    def post(self,request,*args, **kwargs):

        print(dict(request.POST.items()))
        form = TaskManualForm(request.POST)
        if form.is_valid() :
            print('its ok')
            print(form.cleaned_data['title'])
            print(form.cleaned_data['description'])
            print(form.cleaned_data['priority'])
            #   save cleaned_data .....   
            return HttpResponse("hooorrraaaa")
            # return redirect(reverse('tasks_list'))
        else :  return JsonResponse(form.errors)


        return HttpResponse("this is post method on taskView")

# # end step 2


# use forms.Models
#step 3
# class TasksView(View):

#     def get(self,request,*args, **kwargs):
#         form = TaskForm() #MODEL FORM
        
#         tasks = Task.objects.all()
#         return render(request,'lists_step2.html',{'tasks': tasks,'form':form})

#     def post(self,request,*args, **kwargs):

#         form = TaskForm(request.POST)
#         if form.is_valid() :
#             print('its ok')
#             print(form.cleaned_data['title'])
#             print(form.cleaned_data['description'])
#             print(form.cleaned_data['priority'])
#             form.save()
#             # return HttpResponse("hooorrraaaa")
#             return redirect(reverse('tasks_list'))
#         else :  return JsonResponse(form.errors)


#         return HttpResponse("this is post method on taskView")

# end step 3

#  end of steps 
# ############################################

# این صفحه یه باگ کوچولو داره صفحه بندی داره ولی صفحه بندی اعمال نمیشه باید چکار کنیم تا درست بشه ؟
def sample_paginator(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 2) # Show 2 contacts per page.   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    task_list = paginator.page(paginator.num_pages)
    return render(request, 'pagination.html', {'task_list':task_list,'page_obj': page_obj})



from django.views.generic import ListView

#  plz try with ListView
# لینک های زیر رو بخونید حتما
# refrence Link : https://docs.djangoproject.com/en/3.2/topics/pagination/
# other refrence : https://djangocentral.com/adding-pagination-with-django/

# class ContactListView(ListView):
#     paginate_by = 2
#     model = Task


def dynamic(request):
    if request.method == "POST" : 
        print(dict(request.POST.items()))
        tasks = json.loads(request.POST['tasks'])
        # print()
        print(type(tasks))
    
    return render(request, 'dynamic.html',{})




def maktabsample(request):
    if request.method == "POST" :
        print('hooorrraaaa')
        print(dict(request.POST.items()))
        print(request.POST['title'])
        print(request.POST['description'])
        print(request.POST['priority'])
        # if(len(request.POST['title']) > 10 or len(request.POST['descrition'])>100 ):
        #     HttpResponse('طول تایتل یا دسک زیاده')
        task = Task(title=request.POST['title'],description =request.POST['description'],priority=request.POST['priority'] )
        task.save()
        return HttpResponse("خدا خیرت بده سیو شد:)")


    tasks = Task.objects.all()
    return render(request, 'maktab51.html',{'tasks': tasks})



def simple(request):
    form = simpleForm(request.POST or None)
    if request.method == 'POST':
        print(dict(request.POST.items()))
        print(form.is_valid())
        if form.is_valid() :
            print('hooooraaa')

            print(form.cleaned_data['title'])
            print(form.cleaned_data['description'])
            print(form.cleaned_data['number'])
            
            # save data :)
            return HttpResponse("دمت گرم !")
            

        else : 
            print(form.cleaned_data)
            print(form.errors) #TODO : show error on page 
            return HttpResponse("form not valid")

    else : 

        # form = simpleForm()

        return render(request, 'maktab51_form.html',{'form': form})




class aboutView(TemplateView):
    template_name="about.html"



class tasksListViews(ListView):
    model = Task
    queryset = Task.objects.filter(title__contains = 's').order_by('-date_of_creation')
    context_object_name = 'my_tasks'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = ['book1','book2','book3']
        pprint(context)
        return context

    
class tasksDetailViews(DetailView):
    # نمایش جزییات تسک ها
    # ما میتوانیم از این کلاس جهت نمایش جزییات لیست استفاده کنیم 
    
    model = Task
    # queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pprint(context)   
        return context
