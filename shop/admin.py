from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Product, AdvUser

@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('is_active'),
              ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'description', ('price', 'quantity'), 'user')
    list_display = ('title', 'quantity')
