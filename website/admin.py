from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserForm, CreateUserForm

class CustomUserAdmin(UserAdmin):
    # Your other attributes here
    form = UserForm
    add_form = CreateUserForm
    ordering=("email",)

admin.site.register(User, CustomUserAdmin )