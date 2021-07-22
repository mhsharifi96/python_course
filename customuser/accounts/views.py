from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login


from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def simpleLogin(request):
    if request.method == "POST" :
        print(request.POST['username'])
        print(request.POST['password'])
        user = authenticate(username =request.POST['username'],password = request.POST['password'] )
        if user is not None : 
            login(request,user)
            return redirect(reverse('home'))
        return HttpResponse('login fail')

    else :
        return render(request, 'simpleLogin.html',{})