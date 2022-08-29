from django.contrib import admin

from .models import Customer, Owner, User

# Register your models here.
admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Customer)