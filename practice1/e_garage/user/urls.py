from django.urls import path, include
from user import views
from .views import UserLoginForm, UserRegistrationForm

app_name = 'user_urls'

urlpatterns = [
    path('user-registration/', UserRegistrationForm.as_view(), name='user_registration'),
    path('user-login/', UserLoginForm.as_view(), name = 'user_login'),
    path('index/', views.index, name='index'),
    path('student_detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('student_detail/', views.student_list, name='student_list'),
    path('customer_create/', views.customer_create),
]
