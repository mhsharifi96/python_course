from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy,reverse
from django.views import View

from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreationForm

from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


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




class LoginRequiredTest(LoginRequiredMixin,TemplateView):
    template_name='test.html'


@login_required
def testLogin(request):

    return render(request, 'test.html')

from django.utils.html import escape


class updateTestView(View):
    def get(self,request,*args, **kwargs):
        print(self.kwargs['pk'])
        print(request.user)
        # پیدا کردن ایتم مورد نظر
        # test.objects.get(....)
        return render(request, 'test.html')
    def post(self,request,*args, **kwargs):
        # دریافت درخواست
        # پاس دادن درخواست به فرم
        # اگر فرم صحیح بود(is_valid)
        # سیو کردن آن
        # ریدایرکت آن / ارسال پیام موفقیت 
        pass