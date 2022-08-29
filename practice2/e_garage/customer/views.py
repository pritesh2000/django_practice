from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserForm
# Create your views here.

class UserRegistrationForm(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'user/user_registration.html'
    success_url = '/user/user-login'

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"] 
        return username + "- User Created Successfully..."

class UserLoginForm(LoginView):
    template_name = 'user/user_login.html'
    success_url = '/user/index.html'

def index(request):
    return render(request, 'user/index.html')

