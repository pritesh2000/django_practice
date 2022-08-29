from django.urls import path, include
from customer import views
from .views import UserLoginForm, UserRegistrationForm

app_name = 'garage_urls'

urlpatterns = [
    path('user-registration/', UserRegistrationForm.as_view(), name='user_registration'),
    path('user-login/', UserLoginForm.as_view(), name = 'user_login'),
    path('index/', views.index, name='index'),
]
