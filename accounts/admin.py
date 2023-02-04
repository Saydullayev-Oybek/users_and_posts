from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from .forms import CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'age', 'country')

admin.site.register(CustomUser, CustomUserAdmin)