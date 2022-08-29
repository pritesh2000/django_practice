from django.urls import path, include
from .views import OwnerSignUpView, CustomerSignUpView, SignUp, index

urlpatterns = [
    path('index/', index, name='index'),
    path('signup/', SignUp, name='signup'),
    path('userapp/signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('userapp/signup/owner/', OwnerSignUpView.as_view(), name='owner_signup'),
]
