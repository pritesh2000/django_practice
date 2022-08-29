from django.urls import path

from .views import CustomerRegistrationView, OwnerRegistrationView, UserLogin

app_name = 'userapp_urls'


urlpatterns = [
    path('owner-registration/', OwnerRegistrationView.as_view(), name='owner_registration'),
    path('customer-registration/', CustomerRegistrationView.as_view(), name='customer-registration'),
    path('login/', UserLogin.as_view(), name="login"),
]
