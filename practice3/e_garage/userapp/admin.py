from django.contrib import admin

from .models import CustomerRegistration, OwnerRegistraion, User

# Register your models here.
admin.site.register(User)
admin.site.register(OwnerRegistraion)
admin.site.register(CustomerRegistration)