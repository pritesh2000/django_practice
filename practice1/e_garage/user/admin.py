from django.contrib import admin

from .models import Customer, Student, User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "password", "email", "phone_number", "is_superuser", "is_staff", "is_active", "first_name", "last_name")
    list_display = ("username", "email", "is_staff")
    list_filter = ("is_staff", "created_at", "updated_at")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id",'name']
