from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm


from django.urls import reverse_lazy,reverse
from django.views import generic
from .forms import registerFormModel


class SignUpView(generic.CreateView):
    # custom form (MODELFROM)
    # form_class = UserCreationForm
    # form_class = customForms
    form_class = registerFormModel
    success_url = reverse_lazy('login')
    # success_url = reverse('login')   چرا این خطا میده :) برای شما دوست عزیز
    template_name = 'registration/signup.html'