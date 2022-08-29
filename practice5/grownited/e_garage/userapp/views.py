from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, OwnerSignUpForm
from userapp.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'register.html')


class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        return redirect('index')

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')