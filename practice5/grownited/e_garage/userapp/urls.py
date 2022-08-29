from django.urls import path
from .views import CustomerSignUpView, index, signup, OwnerSignUpView

urlpatterns = [
    path('index/', index, name='index'),
    path('signup/', signup, name='signup'),
    path('user/signup/owner/', OwnerSignUpView.as_view(), name="owner_signup"),
    path('user/signup/customer/', CustomerSignUpView.as_view(), name="customer_signup"),
]
