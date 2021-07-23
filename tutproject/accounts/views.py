from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from django.views import generic


class SignUpView(generic.CreateView):
    # custom form (MODELFROM)
    form_class = UserCreationForm

    success_url = reverse_lazy('login')
    # success_url = reverse('login')
    template_name = 'registration/signup.html'