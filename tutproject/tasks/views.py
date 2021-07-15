from django.shortcuts import  render, redirect, reverse
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views import  View
from django.views.generic import ListView

from django.core.paginator import Paginator


from .models import  Task
from .forms import TaskForm,TaskManualForm,ExampleForm
from django.template import RequestContext

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
# class TasksView(View):

#     def get(self,request,*args, **kwargs):
#         form = TaskManualForm()
#         # form = ExampleForm()
#         print('this get page')
#         tasks = Task.objects.all()
#         return render(request,'lists_step2.html',{'tasks': tasks,'form':form})

#     def post(self,request,*args, **kwargs):

#         print(dict(request.POST.items()))
#         form = TaskManualForm(request.POST)
#         if form.is_valid() :
#             print('its ok')
#             print(form.cleaned_data['title'])
#             print(form.cleaned_data['description'])
#             print(form.cleaned_data['priority'])
#             #   save cleaned_data .....   
#             return HttpResponse("hooorrraaaa")
#             # return redirect(reverse('tasks_list'))
#         else :  return JsonResponse(form.errors)


#         return HttpResponse("this is post method on taskView")

# # end step 2


# use forms.Models
#step 3
class TasksView(View):

    def get(self,request,*args, **kwargs):
        form = TaskForm()
        
        tasks = Task.objects.all()
        return render(request,'lists_step2.html',{'tasks': tasks,'form':form})

    def post(self,request,*args, **kwargs):

        
        form = TaskForm(request.POST)
        if form.is_valid() :
            print('its ok')
            print(form.cleaned_data['title'])
            print(form.cleaned_data['description'])
            print(form.cleaned_data['priority'])
            form.save()
            # return HttpResponse("hooorrraaaa")
            return redirect(reverse('tasks_list'))
        else :  return JsonResponse(form.errors)


        return HttpResponse("this is post method on taskView")

# end step 3



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