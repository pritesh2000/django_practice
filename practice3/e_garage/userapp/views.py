from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from .forms import CustomerRegistrationForm, OwnerRegistrationForm
from django.contrib.auth import login,logout
from .models import User

# Create your views here.


class OwnerRegistrationView(CreateView):
    model = User
    form_class = OwnerRegistrationForm
    template_name = 'ownerportal/registration.html'
    success_url = '/userapp/login'

    def form_valid(self, form):
        user = form.save()
        login(self.request,User)
        user.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        kwargs['user_type']='owner'
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["owner"]
        return username + "- Owner Created Successfully..."

class CustomerRegistrationView(CreateView):
    model = User
    form_class = CustomerRegistrationForm
    template_name = 'userportal/registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, User)
        user.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs['user_type']='customer'
        return super().get_context_data(**kwargs)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["customer"]
        return username + "- Customer Created Successfully..."

class UserLogin(LoginView):
    template_name = 'userportal/login.html'

    def get(self, request, *args, **kwargs):
        print(self.request.user)
        return self.render_to_response(self.get_context_data())
