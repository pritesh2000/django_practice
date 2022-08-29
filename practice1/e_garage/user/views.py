import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from .forms import UserForm
from .models import Student

from .serializers import CustomerSerializer, StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serial = StudentSerializer(student)

    return JsonResponse(serial.data)

    # jackson = JSONRenderer().render(serial.data)
    # return HttpResponse(jackson, content_type='application/json')

def student_list(request):
    student = Student.objects.all()
    serial = StudentSerializer(student, many=True)

    return JsonResponse(serial.data, safe=False)    

    # jackson = JSONRenderer().render(serial.data)
    # return HttpResponse(jackson, content_type='application/json')
print("Csrf before")
@csrf_exempt
def customer_create(request):
    print("Customer Function Calling....")
    if request.method == "post":
        json_data = request.body
        print("json data", json_data, "views.py")
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serial_aiser = CustomerSerializer(data = python_data)

        if serial_aiser.is_valid():
            print("serial_aiser")
            serial_aiser.save()
            mes = {'msg':"Data Created"}
            jsonn = JSONRenderer().render(mes)
            return HttpResponse(jsonn, content_type="application/json")

        jsonn = JSONRenderer().render(serial_aiser.errors)
        return HttpResponse(jsonn, content_type="application/json")

    else:
        return HttpResponse("Customer not created")

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
    success_url = '/user/index'

def index(request):
    return render(request, 'user/index.html')

